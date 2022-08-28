from gpiozero import MotionSensor
from picamera import PiCamera
import os
import subprocess
import time
import datetime
import logging
from gofileHelper import gofileHelper


# GPIO pin number that is connected to the PIR signal pin
PIR_PIN = 4

# Configure the logging system
dirname = os.path.dirname(__file__)
logging.basicConfig(
    filename=os.path.join(dirname, "app.log"),
    level=logging.INFO,
    format="%(levelname)s:%(asctime)s:%(message)s",
)


def main(inactiveDuration=5, outdir="/dev/shm/"):
    """
    Parameters
    ----------
    inactiveDuaration : int
        specifies when the camera should stop recording after no motion has been detected
    outdir : str, default="/dev/shm/"
        the path to the desired directory of which to save the video files. The default is
        a tmpfs path, which should save to ram instead of using disk.

    Returns
    -------
    None
    """
    goHelp = gofileHelper()
    camera = PiCamera()
    pir = MotionSensor(PIR_PIN)

    logging.info("Initializating Camera....")
    camera.resolution = (680, 480)  # units are in pixels

    while True:
        logging.info("Waiting for motion...")
        pir.wait_for_motion()

        # determine recording path
        outfilename = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        h264_path = os.path.join(outdir, outfilename) + ".h264"
        mp4_path = os.path.join(outdir, outfilename) + ".mp4"

        logging.info("Motion detected\nRecording...")
        camera.start_recording(h264_path)
        pir.wait_for_no_motion()
        time.sleep(inactiveDuration)

        logging.info(f"Saving recording to {h264_path}")
        camera.stop_recording()

        logging.info("convert h264 recording to mp4")
        h264_to_mp4(h264_path)

        assert os.path.exists(mp4_path), "MP4 file must be created"

        logging.info("Upload file to gofile")
        goHelp.upload_file(mp4_path)

        logging.info(f"Deleting recording files")
        os.remove(h264_path)
        os.remove(mp4_path)


def h264_to_mp4(path):
    """Convert a h264 video to a mp4 format. Saves it in the same directory
    as the original h264 location.

    Paramters
    ---------
    path : str
        path to the h264 video file

    Output
    ------
    None
    """
    subprocess.run([f"MP4Box -add {path} {path[:len(path)-5] + '.mp4'}"], shell=True)


if __name__ == "__main__":
    main()

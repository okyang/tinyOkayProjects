"""
# Setup
- pip3 install nanpy
# Resources
- https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6
- https://picamera.readthedocs.io/en/release-1.13/recipes1.html
- https://pypi.org/project/nanpy/
"""

import RPi.GPIO as GPIO
from picamera  import PiCamera
import time
import datetime
from nanpy import ArduinoApi, SerialManager

def main(pir_pin=2,inactiveDuration=10,outdir="."):
    """
    *Parameters*
    > `pir_pin<int>`: the GPIO signal pin (in BCM mode) of the PIR motion sensor
    > `inactiveDuaration<int>`: specifies when the camera should stop recording after no motion has been detected
    > `outdir<str>`: the path to the desired directory of which to save the video files
    """
    # === Local Variables ===
    camera = PiCamera()

    # === setup Arduino ===
    connection = SerialManager()
    a = ArduinoApi(connection=connection)

    # === start main loop ===
    while True:
        # === sense PIR motion ===
        motionDetected = a.digitalRead(pir_pin)
        print(motionDetected)

        # === condition ===
        if  motionDetected:
            print("started recording...")

            # === start recording ===
            # Set-up camera
            camera.resolution = (1024,768)

            # Start camera
            camera.start_preview()

            # Camera warm-up time
            time.sleep(2)

            # Determine output filename
            outfilename = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".h264"

            # Start Recording
            camera.start_recording(outdir+"/"+outfilename)

            while motionDetected:

                # record for duration
                time.sleep(inactiveDuration)

                # detected motion
                motionDetected = a.digitalRead(pir_pin)

            # Stop Recording
            camera.stop_recording()
            print("recording finished")

if __name__ == "__main__":
    main(pir_pin=2,inactiveDuration=60,outdir="/media/pi/OKAY")

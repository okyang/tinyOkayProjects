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

# === global variables === 
camera = PiCamera()


def arduinoPirSense(pir_pin=2):
    """
    """
    connection = SerialManager() #SerialManager(device='/dev/ttyUSB0')
    a = ArduinoApi(connection=connection)
    a.pinMode(pir_pin, a.INPUT)
    return a.digitalRead(pir_pin)

def main(pir_pin=2,duration=10,outdir="."):
    """
    *Parameters*
    > `pir_pin<int>`: an int representing the GPIO signal pin (in BCM mode) of the PIR motion sensor
    """
    # === define local parameters ==

    # === set up GPIO ===
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(pir_pin, GPIO.IN)

    # === start main loop ===
    while True:
        # === sense PIR motion ===
        motionDetected = arduinoPirSense(pir_pin)
        print(motionDetected)

        # === conditional for motion capture ===
        if motionDetected:
            print("started recording...")
            # === start recording ===
            record(duration,outdir)
            print("recording finished")
        else:
            pass

def record(duration,outdir="."):
    """
    Uses the Raspbery Pi v2 camera to record videos. Will automatically save files
    according to `outdir` and the datetimestamp.

    *Parameters*
    > `duration<int>`: the number of seconds to record video
    > `outdir<str>`: the filepath directory to save the video file
    """

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

    # record for duration
    time.sleep(duration)

    # Stop Recording
    camera.stop_recording()

if __name__ == "__main__":
    main(pir_pin=2,duration=60,outdir="/media/pi/OKAY")

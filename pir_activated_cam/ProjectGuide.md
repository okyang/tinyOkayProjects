# Motion Activated Raspberry Pi Camera :camera: with PIR and NanPy

This project records videos whenever there is any motion detected. This could be used as a snacks stash security camera, a backyard wildlife monitor, and more. 

## Materials
- Raspberry Pi 3 B+
- Arduino Nano
- Raspberry Pi Camera v2 
- PIR Motion Sensor
- USB Drive (Optional)

We will use a PIR motion sensor that is connected to the Arduino Nano via its GPIO pins. The Arduino Nano will serve as a "slave" unit (unfortunantely, that's just the term used by nanPy and other electrical engineers) to the Raspberry Pi through serial communication. Through serial communication, the Raspberry Pi will know when the PIR sensor detects motion and trigger the Raspberry Pi Camera to start recording a video. 

## Prequisites
- Raspberry Pi Debian OS already setup on Raspberry Pi

I listed specific versions

## Instructions 


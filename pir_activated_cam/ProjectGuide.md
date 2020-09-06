# Motion Activated Raspberry Pi Camera :camera: (with PIR and NanPy)

This project records videos whenever there is any motion detected. This could be used as a snacks stash security camera, a backyard wildlife monitor, and more. My Raspberry Pi had some issues with its GPIO pins and I also learned that some specific sensors do not work will with the Pi. So I decided this was the perfect opportunity to also learn how to use NanPy, which allows the Raspberry Pi to use the Arduino's GPIO pins.

## Materials
- Raspberry Pi 3 B+
- Arduino Uno
- Raspberry Pi Camera v2
- PIR Motion Sensor
- USB Drive (Optional)
- Jumper Wires

I listed specific versions of some of the materials because that is what I tested it on. Other versions will probably work, but I do not guarantee it.

## How it works

We will use a PIR motion sensor that is connected to the Arduino Nano via its GPIO pins. The Arduino Nano will serve as a "slave" unit (unfortunately, that's just the term used by nanPy and other electrical engineers) to the Raspberry Pi through serial communication. Through serial communication, the Raspberry Pi will know when the PIR sensor detects motion and trigger the Raspberry Pi Camera to start recording a video.

## Prerequisites
- Raspberry Pi Debian OS already setup on Raspberry Pi
- Basic understanding of using the command line
- Raspberry Pi Camera Attached to Pi and Camera Interfacing Option Enabled
- Basic understanding of GPIO pins

## Instructions
1. Wiring the Circuit
> **For this step make sure the power is off.**
>
> **a.** Using female to male jumper wires make the following PIR sensor to Arduino connections:
>
> - V+ <--> 5V
> - GND <--> GND
> - Signal <--> D2 (Digital Pin 2)

2. Setup Software Dependencies
> **a.** Power up the Pi and open the terminal
>
> **b.** clone this directory using:
>
> `git clone https://github.com/okyang/tinyOkayProjects.git`
>
> or just download the code from [here](https://github.com/okyang/tinyOkayProjects.git)
>
> **c.** Make sure to take a note of your path. You can use
3.  Run the Code



## Resources

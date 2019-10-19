# Raspberry-Pi-Drone-and-Flight-Camera-Module

Raspberry Pi Camera module intended for Drone/Flight devices.

## Requirements:
- Raspberry Pi Model 3 B+
- Raspberry Pi Camera Module
- picamera module (pre-installed with raspbian)
- time module (pre-installed with raspbian)
- os module (pre-installed with raspbian)
- random module (pre-installed with raspbian)
- USB (32GB+ Recommended for lengthy projects)*

*You can use the Raspberry Pi as the directory to save folders, but this is not recommended, unless if you're SD card can fit
multiple videos during unhandled flight.

## Setup:

1) Bootup Raspberry Pi
2) Clone/Download the repository
3) Open python file, and replace the "path" variable with the raspberry pi to your USB.
4) Check if the USB path is correct, and change opacity & time settings to your liking.

## How it works:

1) Program intializes picamera module, and checks if the USB directory exists.
2) In the directory set, check if there is already a folder that exists with the set video name ('folder' in this case), if there is, iterate, until the folder name does not exist, set folder name as 'folder#' (# replaced with highest folder number).
3) In video directory, do the same execution as setting a folder directory.
4) Run Camera Module using opacity and time settings, save video as 'video#.h264', and repeat step 3, until the program is interrupted.




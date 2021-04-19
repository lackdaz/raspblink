# !/bin/python
# Simple script for shutting down the Raspberry Pi at the press of a button.

import time
import os
import RPi.GPIO as GPIO
from raspblink import PowerButton

# Use the Broadcom SOC Pin numbers
# Setup the pin with internal pullups enabled and pin in reading mode.

# Turn on power button
power_button = PowerButton()
power_button.switch_on()

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)

# Our function on what to do when the button is pressed
def shutdown(channel):
    print("Shutting Down")
    time.sleep(5)
    os.system("sudo shutdown -h now")


# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(3, GPIO.FALLING, callback=shutdown, bouncetime=2000)

# Now wait!
while 1:
    time.sleep(1)

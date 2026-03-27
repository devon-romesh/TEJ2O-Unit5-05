"""
Created by: Devon
Created on: Mar 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel

# variables 
lightLevels = 0
myNeopixelStrip = neopixel.NeoPixel(pin16, 4)

# setup
display.show(Image.HAPPY)
myNeopixelStrip.clear()
myNeopixelStrip.show()

# runs Button A
while True:
    if button_a.is_pressed():
        lightLevels = display.read_light_level()
        myNeopixelStrip.clear()

        # if lightLevels is more than 52
        if lightLevels > 52:
            myNeopixelStrip[0] = (255, 255, 255) 

        # if lightLevels is more than 104
        if lightLevels > 104:
            myNeopixelStrip[1] = (255, 255, 255)

        # if lightLevels is more than 156
        if lightLevels > 156:
            myNeopixelStrip[2] = (255, 255, 255)

        # if lightLevels is more than 208 
        if lightLevels > 208:
            myNeopixelStrip[3] = (255, 255, 255)

        myNeopixelStrip.show()
        display.scroll("Light level is " + (lightLevels))

    if button_b.is_pressed():
        display.clear()
        myNeopixelStrip.clear()
        myNeopixelStrip.show()
        display.show(Image.HAPPY)

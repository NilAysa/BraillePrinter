#!/usr/bin/python3

import RPi.GPIO as GPIO
from axis import *
from solenoid import *
from text_processing import *
from gui import BraillePrinterGUI
from resources import BrailleAlphabet
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def printBraille(text):
    try:
        text = toMachineBraille(text)
    
        if len(text) > numOfLines:
            print("Text is too long")
            return

        for line in text:
            for i in [0, 1, 2]:
                for letter in line:
                    for j in [1, 0]:
                        if BrailleAlphabet[letter][i][j]:
                            z.push()
                            z.push()
                            print(".", end = "")
                        else:
                            print(" ", end = "")
                        time.sleep(.5)
                        x.goForward(181) #2.5mm
                    print("|", end = "")
                    x.goForward(50) #1.0mm
                print("")
                x.startPosition()
                y.goForward(400) #2.5mm
            print("")
            y.goForward(800) #5mm
        y.startPosition()
    except KeyboardInterrupt:
        x.startPosition()
        y.startPosition()

x = Axis(6,13,19,26)
y = Axis(12,16,20,21)
z = Solenoid(18) 
BraillePrinterGUI(printBraille)




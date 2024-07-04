import RPi.GPIO as GPIO
import time


class Solenoid:
    
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, 0)
        
    def push(self):
        GPIO.output(self.pin, 1)
        time.sleep(.5)
        GPIO.output(self.pin, 0)
        time.sleep(.5)
        
    def __del__(self):
        GPIO.output(self.pin, 0)
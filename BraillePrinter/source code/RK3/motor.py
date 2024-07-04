import RPi.GPIO as GPIO
import time


class Motor:
    sequence = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    
    def __init__(self, pinA, pinB, pinC, pinD):
        self.pins = [pinA, pinB, pinC, pinD]
        self.direction = 1
        self.state = 0
        
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
     

    def setDirection(self, d):
        self.direction = 1 if d > 0 else -1


    def run(self, steps):
        for _ in range(steps):

            self.state += self.direction

            if self.state == -1:
                self.state = 3
            elif self.state == 4:
                self.state = 0
    
            GPIO.output(self.pins, self.sequence[self.state])
            time.sleep(0.0032)
            
        GPIO.output(self.pins, [0, 0, 0, 0])
            

    def __del__(self):
        for pin in self.pins:
            GPIO.output(pin, 0)

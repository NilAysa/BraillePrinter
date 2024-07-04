from motor import Motor

class Axis:
    def __init__(self, pinA, pinB, pinC, pinD):
        self.motor = Motor(pinA, pinB, pinC, pinD)
        self.stepsTaken = 0
    
    def goForward(self, steps):
        self.stepsTaken += steps
        self.motor.run(steps)

    def startPosition(self):
        self.motor.setDirection(-1)
        self.motor.run(self.stepsTaken)
        self.motor.setDirection(1)
        self.stepsTaken = 0
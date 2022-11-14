class Particle():
    def __init__(self, x, y, xVel = 0, yVel = 0, xAccel = 0, yAccel = 0, tang = True):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.tang = tang

        
import numpy as np


class CSolid:
    def __init__(
        self,
        x=0,
        y=0,
        radius=0,
        xVel=0,
        yVel=0,
        xAccel=0,
        yAccel=0,
        mass=0,
    ):
        self.xPos = x
        self.yPos = y
        self.radius = radius
        self.xVel = xVel
        self.yVel = yVel
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.mass = mass

    def __str__(self):
        properties = f"\n\
                     \n The x-position is {self.x}, the y-position is {self.y}.\
                     \n The x-velocity is {self.xVel}, the y-velocity is {self.yVel}.\
                     \n The x-acceleration is {self.xAccel}, the y-acceleration is {self.yAccel}.\
                     \n The mass is {self.mass}, the radius is {self.radius}."
        return properties

    def calculateArea(self):
        center = (self.xPos, self.yPos)

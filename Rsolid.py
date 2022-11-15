class Rsolid:
    def __init__(
        self,
        x=0,
        y=0,
        length=1,
        width=1,
        xVel=0,
        yVel=0,
        xAccel=0,
        yAccel=0,
        mass=0,
    ):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
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
                     \n The mass is {self.mass}."
        return properties
    def checkCollision(self, RSolid2):
        return False
    def collisionResult(self, RSolid2):
        return None
        
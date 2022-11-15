class solid:
    def __init__(
        self,
        x=0,
        y=0,
        leng=1,
        wid=1,
        xVel=0,
        yVel=0,
        xAccel=0,
        yAccel=0,
        fric=0,
        mass=0,
        tang=True,
        sticky=False,
        rigid=False,
    ):
        self.x = x
        self.y = y
        self.leng = leng
        self.wid = wid
        self.xVel = xVel
        self.yVel = yVel
        self.xAccel = xAccel
        self.yAccel = yAccel
        self.fric = fric
        self.mass = mass
        self.tang = bool(tang)
        self.sticky = bool(sticky)
        self.rigid = bool(rigid)

    def __str__(self):
        properties = f"\n\
                     \n The x-position is {self.x}, the y-position is {self.y}.\
                     \n The x-velocity is {self.xVel}, the y-velocity is {self.yVel}.\
                     \n The x-acceleration is {self.xAccel}, the y-acceleration is {self.yAccel}.\
                     \n The friction is {self.fric}, the mass is {self.mass}.\
                     \n The object's tangibility is {self.tang}, it's stickiness is {self.sticky}, and the rigidity is {self.rigid} "
        return properties

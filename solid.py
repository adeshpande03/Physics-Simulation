class Solid:
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
        tang=True,
        fric=0,
        mass=0,
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
        self.tang = tang
        self.fric = fric
        self.mass = mass
        self.sticky = sticky
        self.rigid = rigid

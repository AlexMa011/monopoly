class zone():
    def __init__(self):
        self.money=0
        self.diamond=0
        self.owner=0
        self.size=0
        self.x=0
        self.y=0
        self.direction='v'
        self.name='zone'

    def __str__(self):
        return "%i %i"%(self.money,self.diamond)


class cell():
    def __init__(self,zone):
        self.money=zone.money
        self.diamond=zone.diamond
        self.area=zone
        self.grade=0
        self.x=zone.x
        self.y=zone.y

class bank():
    def __init__(self):
        self.x=240
        self.y=0

class supermarket():
    def __init__(self):
        self.x=0
        self.y=0


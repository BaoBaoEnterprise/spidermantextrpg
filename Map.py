class CurrentLocation:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getdescription(self):
        if self.x == 0 and self.y == 0:
            print("Spiderman is in the starting zone! Coordinates : x={0} y={1}".format(self.x, self.y))
        else:
            print("Spiderman is in location x={0} y={1}".format(self.x, self.y))

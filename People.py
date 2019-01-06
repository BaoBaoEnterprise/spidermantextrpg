class Person:

    def __init__(self, name, level, strength, agility, charm, hitpoints):
        self.name = name
        self.level = level
        self.strength = strength
        self.agility = agility
        self.charm = charm
        self.hitpoints = hitpoints

    def jump(self):
        print(self.name + " jumped up really high!")

    def move(self, direction):
        """map"""

    def fight(self, badguy):
        if self.strength > badguy.strength:
            badguy.hitpoints = badguy.hitpoints - self.strength
            if badguy.hitpoints <= 0:
                print("Spiderman killed " + badguy.name)
            else:
                print("You punched {0} in the face!.  {0} has {1} hitpoints left!".format(badguy.name, badguy.hitpoints))
        else:
            print("Spiderman got killed by " + badguy.name)
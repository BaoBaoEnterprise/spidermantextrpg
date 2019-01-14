from Map import CurrentLocation
import random

class Person:

    def __init__(self, name, level, strength, agility, charm, hitpoints, currentlocation):
        self.name = name
        self.level = level
        self.strength = strength
        self.agility = agility
        self.charm = charm
        self.hitpoints = hitpoints
        self.currentlocation = currentlocation

    def jump(self):
        print(self.name + " jumped up really high!")

    def move(self, direction):
        if direction == 'w':
            self.currentlocation.x -= 1
        elif direction == 'e':
            self.currentlocation.x += 1
        elif direction == 's':
            self.currentlocation.y -= 1
        elif direction == 'n':
            self.currentlocation.y += 1
        else:
            print("INVALID DIRECTION IDIOT!")

    def fight(self, badguy):
        if self.strength > badguy.strength:
            badguy.hitpoints = badguy.hitpoints - self.strength
            if badguy.hitpoints <= 0:
                print("Spiderman killed " + badguy.name)
            else:
                print("You punched {0} in the face!.  {0} has {1} hitpoints left!".format(badguy.name, badguy.hitpoints))
        else:
            print("Spiderman got killed by " + badguy.name)

class BadGuy(Person):

    def __init__(self, level, currentlocation):
        str = random.randint(1*level, 2*level)
        agility = random.randint(1* level, 2*level)
        charm = random.randint (1* level, 2*level)
        hitpoints = random.randint (1* level, 2*level)

        '''name = ["Vulture", "Doctor Octopus", "Beetle", "Lizard", "Rhino", "Scorpion", "Black cat"]'''
        Person.__init__(self, "Charles", level, str, agility, charm, hitpoints, currentlocation)



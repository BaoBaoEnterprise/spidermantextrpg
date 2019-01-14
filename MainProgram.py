from People import Person
from People import BadGuy

import People
from Map import CurrentLocation

currentlocation = CurrentLocation(0, 0)


spiderman = Person(name='Peter Parker', level=1, agility=10, charm=15, strength=12, hitpoints=10, currentlocation=currentlocation)



"""while spiderman.hitpoints > 0:
    print(spiderman.currentlocation.getdescription())
    command = input("Tell us what you want Spiderman to do \n >> ")
    if command == "jump":
        spiderman.jump()
    elif command.startswith("fight"):
        spiderman.fight(People.createbadguy(spiderman.level, spiderman.currentlocation))
    elif command.startswith("move"):
        direction = input("What direction do you want to move \n >>")
        spiderman.move(direction)"""


badguy1 = BadGuy(10, spiderman.currentlocation)

print(badguy1.strength)



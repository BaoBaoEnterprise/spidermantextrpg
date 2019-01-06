from People import Person

spiderman = Person(name='Peter Parker', level=1, agility=10, charm=15, strength=12, hitpoints=10)

badguys = []
badguys.append(Person(name='Rufus Mcgee', level=1, strength=2, agility=1, charm=3, hitpoints=20))

print("Hey everybody... it's SPIDERMAN!  Rufus Mcgee wants to fight you!")



while spiderman.hitpoints > 0:
    command = input("Tell us what you want Spiderman to do \n >> ")
    if command == "jump":
        spiderman.jump()
    elif command.startswith("fight"):
        spiderman.fight(badguys[0])

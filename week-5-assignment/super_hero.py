class SuperHero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power
        self.__level = level

    def describe(self):
        return f"{self.name} has the power of {self._power}"

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        print(f"{self.name} leveled up to {self.__level}")

class FlyingHero(SuperHero):
    def fly(self):
        print(f"{self.name} is soaring through the skies")

class StrongHero(SuperHero):
    def punch(self):
        print(f"{self.name} smashes with incredible strength")

# Instantiate heroes
hero1 = FlyingHero("SkyBolt", "Flight", 3)
hero2 = StrongHero("IronMan", "Super Strength", 5)

# Use the methods
print(hero1.describe())
hero1.fly()
hero1.level_up()

print(hero2.describe())
hero2.punch()
hero2.level_up()

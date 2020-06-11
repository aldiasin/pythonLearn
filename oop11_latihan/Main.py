class Hero:

    # private class variabel
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStd = health
        self.__attPowStd = attPower
        self.__armorStd = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStd * self.__level
        self.__attPow = self.__attPowStd * self.__level
        self.__armor = self.__armorStd * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{}\n\tattact = {}\n\tarmor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPow, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStd * self.__level
            self.__attPow = self.__attPowStd * self.__level
            self.__armor = self.__armorStd * self.__level

    def attack(self,musuh):
        self.gainExp = 50


slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)

class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    #getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    #setter
    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttPower(self,nilaiBaru):
        self.__attackPower = nilaiBaru

#awal game
sven = Hero("sven",100,4)

#game berjalan
print(sven.getName())
print(sven.getHealth())
sven.diserang(5)
print(sven.getHealth())
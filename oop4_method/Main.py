class Hero: #template
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #void function / method tanpa return
    def siapa(self): #pakai self karena nempel sama heronya
        print("namaku adalah " + self.name)

    #method dgn argumen
    def healthUp(self,up):
        self.health += up

    #method dgn return
    def getHealth(self):
        return self.health


hero1 = Hero('sniper',100,10,4)
hero2 = Hero('mirana',90,5,8)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
print(hero1.health)
hero1.healthUp(5)

print(hero1.getHealth())

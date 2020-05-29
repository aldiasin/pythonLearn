class Hero:

    def __init__(self,name,health,attactPower,armorNumber):
        self.name = name
        self.health = health
        self.attactPower = attactPower
        self.armorNumber = armorNumber

    def attack(self,enemy):
        print(self.name + ' attack ' + enemy.name)
        enemy.attacked(self, self.attactPower)

    def attacked(self,enemy,attactPower_enemy):
        print(self.name + ' attacked by ' + enemy.name)
        attack_get = attactPower_enemy/self.armorNumber
        print('attack hit : ' + str(attack_get))
        self.health -= attack_get
        print('health ' + self.name + ' remaining ' + str(self.health))

razor = Hero('razor',100,10,5)
sven = Hero('sven',100,5,10)

razor.attack(sven)
sven.attack(razor)
razor.attack(sven)
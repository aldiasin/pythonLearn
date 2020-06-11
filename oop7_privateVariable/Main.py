class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #variable instance private
        self.__private = "private"
        #variable instance protected
        self._protected = "protected"


luna = Hero("luna",100)

print(luna.__dict__)
print(Hero.__dict__)
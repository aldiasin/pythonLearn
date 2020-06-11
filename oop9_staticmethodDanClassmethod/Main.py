class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    #Method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    #Method ini tdk berlaku untuk objek tapi untuk class
    # def getJumlah1():
    #     return Hero.__jumlah

    #Method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    #biar lebih elegan pakai ini aja
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sven = Hero('sven')
print(Hero.getJumlah2())
sniper = Hero('sniper')
print(Hero.getJumlah2())
ucup = Hero('ucup')
print(Hero.getJumlah3())
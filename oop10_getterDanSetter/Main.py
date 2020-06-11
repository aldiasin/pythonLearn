class Hero:

    def __init__(self,name,helath,armor):
        self.name = name
        self.__health = helath
        self.__armor = armor
        # self.info = "name : {} \n\thealth: {}".format(self.__name,self.__health)

    # def getHealth(self):
    #     return self.__health

    #merubah method jadi variabel
    @property
    def info(self):
        return "name : {} \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor dihapus')
        self.__armor = None



sven = Hero('sven',100,10)

print('merubah info')
print(sven.info)
sven.name = 'ucup'
print(sven.info)

print('getter dan setter untuk __armor')
print(sven.armor)
print(sven.__dict__)
sven.armor = 50
print(sven.armor)
print(sven.__dict__)

print('hapus armor')
del sven.armor
print(sven.__dict__)

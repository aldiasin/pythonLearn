from Hero import HeroIntellegent,HeroStrength

lina = HeroIntellegent('lina')
slardar = HeroStrength('slardar')

lina.show_info()
slardar.show_info()

lina.gainExp = 200
slardar.gainExp = 250
lina.show_info()
slardar.show_info()
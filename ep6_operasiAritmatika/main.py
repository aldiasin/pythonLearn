a = 10
b = 3

#tambah
hasil = a + b
print(a,"+",b,"=",hasil)

#kurang
hasil = a - b
print(a,"-",b,"=",hasil)

#kali
hasil = a * b
print(a,"*",b,"=",hasil)

#bagi
hasil = a / b #otomatis jadi float
print(a,"/",b,"=",hasil)

#pangkat
hasil = a ** b
print(a,"**",b,"=",hasil)

#sis bagi (modulus)
hasil = a % b
print(a,"%",b,"=",hasil)

#keblaikan modulus (floor division)
hasil = a // b
print(a,"//",b,"=",hasil)

#prioritas operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman"
    4. pertambahan dan teman"
'''

hasil = 3 ** 2 * 4 + 3 / 2 - (2 % 4) // 3
print(3,"**",2,"*",4,"+",3,"/",2,"-","(",2,"%",4,")","//",3,"=",hasil)
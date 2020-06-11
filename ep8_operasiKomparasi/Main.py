a = 4
b = 2

print('====lebih====')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

print('====kurang====')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

print('====lebihSamaDengan====')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print('====kurangSamaDengan====')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print('====SamaDengan====')
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

print('====tidakSamaDengan====')
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

#is membandingkan objeknya (identitas objeknya)
x = 3
y = 3
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)
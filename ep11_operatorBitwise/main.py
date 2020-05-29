a = 9
b = 5

#bitwiseOR (|)
c = a | b
print('====OR====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('nilai:',b,' ,binary:',format(b,'08b'))
print('====|=====')
print('nilai:',c,' ,binary:',format(c,'08b'))

#bitwiseAND (&)
c = a & b
print('====AND====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('nilai:',b,' ,binary:',format(b,'08b'))
print('====&=====')
print('nilai:',c,' ,binary:',format(c,'08b'))

#bitwiseXOR (^)
c = a ^ b
print('====XOR====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('nilai:',b,' ,binary:',format(b,'08b'))
print('====^=====')
print('nilai:',c,' ,binary:',format(c,'08b'))

#bitwiseNOT (~)
c = ~a
print('====NOT====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('====~=====')
print('nilai:',c,' ,binary:',format(c,'08b'))
print('====^=====')
d = 0b0000001001
e = 0b1111111111
print('nilai:',e^d,' ,binary:',format(e^d,'08b'))

#shift right (>>)
c = a >> 1
print('====shiftright====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('====>>=====')
print('nilai:',c,' ,binary:',format(c,'08b'))

#shift right (<<)
c = a << 1
print('====shiftleft====')
print('nilai:',a,' ,binary:',format(a,'08b'))
print('====<<=====')
print('nilai:',c,' ,binary:',format(c,'08b'))
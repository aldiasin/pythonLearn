# a = 10, a adalah variabel bernilai 10

#tipe data:Angka satuan (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data:Angka dengan koma (float)
data_float = 3.14
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#tipe data:Kumpulan karakter (string)
data_string = "si ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#tipe data:Biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

##tipe data:Khusus
#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bhs C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
#rubah tipe data satu ke tipe lain

##integer
print("===dataInteger===")
data_int = 9
print("data = ", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #0 false, lainnya true
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

##float
print("===dataFloat===")
data_float = 9.9
print("data = ", data_float, ", type =", type(data_float))

data_int = int(data_float) #dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #0 false, lainnya true
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

##boolean
print("===dataBoolean===")
data_bool = True
print("data = ", data_bool, ", type =", type(data_bool))

data_int = int(data_bool) #dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) #0 false, lainnya true
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_float, ", type =", type(data_float))

##string
print("===dataString===")
data_str = "13"
print("data = ", data_str, ", type =", type(data_str))

data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #false jika string kososng
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))
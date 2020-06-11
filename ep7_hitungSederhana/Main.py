#konversi suhu

print("==PROGRAM KONVERSI SUHU==")
celcius = float(input('masukkan suhu dalam celcius: '))

#reamur
reamur = (4/5)*celcius
print("suhu ", celcius, " celcius", "dalam reamur adalah ", reamur, "reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print("suhu ", celcius, " celcius", "dalam fahrenheit adalah ", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu ", celcius, " celcius", "dalam kelvin adalah ", kelvin, "kelvin")

#fahrenheit ke kelvin
kelvin2 = float(input('masukkan suhu dalam kelvin: '))
fahrenheit2 = ((9/5)*(kelvin2 - 273)) + 32
print("suhu ", kelvin2, "kelvin", "dalam fahrenheit adalah ", fahrenheit2, "fahrenheit")

#kelvin ke fahrenheit
fahrenheit3 = float(input('masukkan suhu dalam fahrenheit: '))
kelvin3 = ((5/9)*(fahrenheit3-32)) + 273
print("suhu ", fahrenheit3, "fahrenheit", "dalam kelvin adalah ", kelvin3, "kelvin")
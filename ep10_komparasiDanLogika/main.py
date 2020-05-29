#buat gabungan area rentang dari angka

#+++++++3-------10+++++++
inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih dari 10:\n"))

isCorrect = (inputUser < 3) or (inputUser > 10)
print("hasilnya",isCorrect)

#-------3++++++++10------
inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\natau\nkurang dari 10:\n"))

isCorrect = (inputUser > 3) and (inputUser < 10)
print("hasilnya",isCorrect)

#-------0++++++++5--------8+++++++11-------
inputUser = float(input("masukkan angka yang bernilai\ndi antara 0 dan 5\natau\ndi antara 8 dan 11\n"))

isCorrect = ((inputUser > 0) and (inputUser < 5)) or ((inputUser > 8) and (inputUser < 11))
print("hasilnya",isCorrect)

#+++++++0--------5++++++++8-------11+++++++
inputUser = float(input("masukkan angka yang bernilai\nkurang dari 0\natau\ndi antara 8 dan 11\natau\nlebih dari 11\n"))

isCorrect = (inputUser < 0) or ((inputUser > 5) and (inputUser < 8)) or (inputUser > 11)
print("hasilnya",isCorrect)

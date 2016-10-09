# Nama : Kalkulator sederhana v.1.0.0
# Description : Aplikasi kalkulator sederhana, menggunakan fungsi
# 			    dictionary python
# Author : Adi Purnama

while True:
	print("\n=== Kalkulator Sederhana v.1.0.0 ===")
	print("")
	print("Pilih operasi:")
	print("1. Kali")
	print("2. Bagi")
	print("3. Tambah")
	print("4. Kurang")
	print("5. Keluar")

	jawab = int(input("Jawab : "))
	
	if (jawab is 5):
		print("\nTerima kasih!")
		break
	
	angka1 = int(input("\nMasukkan angka pertama : "))
	angka2 = int(input("Masukkan angka kedua : "))
	operasi = {
		1 : angka1*angka2,
		2 : angka1/angka2,
		3 : angka1+angka2,
		4 : angka1-angka2,
		}

	print("\nHasil = ", operasi[jawab])
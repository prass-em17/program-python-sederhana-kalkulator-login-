#pesan welcome
print(">>>>>>>>KALKULATOR SEDERHANA<<<<<<<<")
print("")
print("")

#pin
while True:
    #input pin
    pin = input("Masukkan PIN ")
    if pin == "8888":
        print("PIN Benar, Selamat Datang")
        print("")
        break
    else:
        print("PIN Salah, Masukkan PIN dengan benar ")
        print("")
#pemilihan operasi
print("")
print("")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^OPERASI BILANGAN^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian   (x)")
print("4. Pembagian   (:)")
print("")
print("")
print("Pilih Operasi Bilangan")
print("Contoh :")
print("          3(Untuk Operasi Bilangan Perkalian)")
print("")

plhn = input("Masukkan Pilihan = ")
#penjumlahan
if plhn == "1":
    print("==============================================")
    print("=====^Selamat Datang Di Menu Penjumlahan^=====")
    print("==============================================")
    bil1 = int(input("Masukkan Bilangan 1 = "))
    bil2 = int(input("Masukkan Bilangan 2 = "))
    hslp = bil1 + bil2
    print(bil1, '+' ,bil2,' = ',hslp)
    print(




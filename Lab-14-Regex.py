#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 14 (Regex)

"""Sebuah perusahaan meminta untuk dibuatkan program mengubah nomor telepon ke format yang benar. Perusahaan tersebut menginginkan nomor telepon yang diinput
oleh pengguna dapat langsung diubah ke format yang dia inginkan yaitu tanpa ada simbol/huruf selain +62 yang merupakan kode negara dan panjangnya antara 10 sampai 13 digit

input : 
-jumlah nomor yang ingin diubah
-nomor telepon yang ingin di ubah

proses :
-menghilangkan huruf, simbol, dan spasi
-mengecek apakah angka depan itu 0
-menggati angka 0 di depan menjadi +62
-mengecek panjangnya antara 12-15 digit

output :
-"+62{9-12} mengeprint nomor telepon dan valid
- print nomor telepon dan tidak valid

"""

#CODE
import re

jumlah = int(input("Banyak nomor telepon yang ingin diinput : "))

for i in range (jumlah):
    nomor = input("Masukan nomor telepon : ")
    ganti = re.sub("\W","",nomor)
    ganti = re.sub("[a-zA-Z]","",ganti)
    ganti2= re.sub("^0","+62",ganti)
    cek = re.findall("^0",ganti)
    cek2= re.findall("\d{12,15}$/",ganti2)
    if cek and cek2:
        print(f"Fixed: {ganti2} adalah valid")
    else:
        print(f"Fixed: {ganti2} tidak valid")


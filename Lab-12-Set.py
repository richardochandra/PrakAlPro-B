#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 12 (Set)

"""Panitia perlombaan Desa Teknoju ingin mengadakan lomba. Lombanya yaitu berupa lomba mengetik kata terbanyak dan tidak boleh sama.
Panitia meminta untuk dibuatkan program sederhana untuk lomba tersebut. Program yang diinginkan panitia adalah menampung
hasil ketikan dari peserta lomba, menghapus kata yang sama dan menghitung banyakknya kata yang ditulis dalam waktu tertentu

input = 
-nama
-kata
-kata "stop" untuk berhenti

proses = 
-memasukan setiap inputan kedalam set
-memasukan nama sebagai key dan banyak/panjang set sebagai value (dictionary) 

output =
-kata yang ditulis (dalam set)
-nama dan banyak kata yang ditulis dalam dictionary

"""

#Code

print("Selamat datang pada program lomba ketik cepat")
nama = input("Masukan nama anda : ")
start = input("Tekan Enter setelah aba-aba dari panita untuk memulai mengetik")
print("Start!")
x = set()
abc = "abcdefghijklmnopqrstuvwxyz"
while True:
    kata = input("- ").lower()
    if kata == "stop" :
        break
    else :
        for i in range (len(kata)):
            if kata[i] not in abc :
                break
            elif i == (len(kata)-1) and kata[i] in abc:
                x.add(kata)
print()
x=sorted(x)
d = dict()
d[nama] = len(x)
print(d)
print(f"Semua kata yang ditulis {nama} adalah ")
for i in x :
    print(i)

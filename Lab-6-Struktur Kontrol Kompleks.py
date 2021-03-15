#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 6 (Struktur Kontrol Kompleks)

"""Restoran Serba Ada sedang meningkatkan pelayanannya menggunakan sistem robot pesan namun tidak memiliki pemrograman robot pesan
untuk menerima pesanan dari pelanggan dan pada akhirnya Restoran Serba Ada meminta untuk dibuatkan program tersebut

input :
-makan/minum atau selesai
-jumlah menu (jenis menu)
-makanan/minuman yang ingin dipesan
-jumlahnya

proses :
jumlah makan
jumlah minuman
jenis makan/minum
jumlah makan/minum

output :
menampilkan makanan/minuman apa saja
jumlah total porsi makan/minum
jumlah makan/minum per menu
"""

#CODING 
print("===== RESTORAN SERBA ADA =====")
jumMakan = 0
jumMinum = 0
totMakan = 0
totMinum = 0

while True :
    print("Input'selesai' jika sudah")
    pesan = str(input("Pesan makan atau minum : ")).lower()
    if pesan == "makan":
        jumMakan = int(input("Ingin memesan berapa menu : "))
        pesanMakan = []
        banyakMakan = []
        for i in range (jumMakan):
            pesanan = input("Masukan pesanan anda : ")
            pesanMakan.append(pesanan)
            banyak = input("Berapa banyak yang ingin anda pesan : ")
            banyakMakan.append(banyak)
            totMakan += int(banyak)
    elif pesan == "minum":
        jumMinum = int(input("Ingin memesan berapa menu : "))
        pesanMinum = []
        banyakMinum = []
        for i in range (jumMinum):
            pesanan = input("Masukan pesanan anda : ")
            pesanMinum.append(pesanan)
            banyak = input("Berapa banyak yang ingin anda pesan : ")
            banyakMinum.append(banyak)
            totMinum += int(banyak)
    elif pesan == "selesai":
        break
    else :
        print("Input yang anda masukan salah, harap ulangi inputan anda!")

if jumMakan !=0:
    for i in range (jumMakan):
        print(f"Anda memesan {pesanMakan[i]} sebanyak {banyakMakan[i]}")
elif jumMakan ==0 :
    print("Anda tidak memesan makanan!")
if jumMinum !=0:
    for i in range (jumMinum):
        print(f"Anda memesan {pesanMinum[i]} sebanyak {banyakMinum[i]}")
elif jumMinum ==0 :
    print("Anda tidak memesan minuman!")

if totMakan !=0:
    print(f"Total makanan yang anda pesan {totMakan}")
elif totMakan == 0:
    print("Total makanan yang anda pesan 0")
if totMinum !=0:
    print(f"Total minuman yang anda pesan {totMinum}")
elif totMinum == 0:
    print("Total minuman yang anda pesan 0")

cek = input("Apakah pesanan anda sudah benar (sudah/belum) : ").lower()
if cek == "sudah":
    print("Silahkan tunggu sebentar!")
    print("Pesanan anda sedang disiapkan")
elif cek =="belum":
    print("Silahkan panggil kembali robot pesan kami")
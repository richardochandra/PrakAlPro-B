#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 10 (Dictionary)


"""Restoran Dewe mengalami kesulitan dalam menyampaikan pesanan ke dapur karena masih menggunakan kertas sehingga restoran dewe ingin membuat program untuk
menyampaikan pesanan dari pelanggan yang diterima oleh kasir ke dapur. Pesan yang disampaikan adalah makanan berserta jumlahnya dan minuman beserta jumlahnya.
Bantulah restoran dewe untuk membuat programnya.

input = 
-jumlah makanan
-makanan yang dipesan
-jumlah pesanan (makanan)
-jumlah minuman
-minuman yang dipesan
-jumlah pesanan (minuman)

proses = 
-menjadikan makanan/minuman menjadi key
-jumlah makanan/minuman yang dipesan itu menjadi value

output = 
dict makanan : pesanan
dict minuman : pesanan

"""
#CODE 

makanan = int(input("Masukan jumlah makanan : "))
d_makan = dict()
if makanan > 0:
    for i in range (makanan):
        menu = input("Menu makanan : ")
        jumlah_makan = int(input("Jumlah pesanan : "))
        d_makan[menu] = jumlah_makan

minuman = int(input("Masukan jumlah minuman : "))
d_minum = dict()
if minuman > 0:
    for i in range(minuman):
        menu = input("Menu minuman : ")
        jumlah_minum = int(input("Jumlah pesanan : "))
        d_minum[menu] = jumlah_minum
print()
if makanan == 0 :
    print("Tidak memesan makanan")
else :
    print(f"Makanan yang dipesan {d_makan}")
if minuman ==0 :
    print("Tidak memesan minuman")
else :
    print(f"Minuman yang dipesan {d_minum}")
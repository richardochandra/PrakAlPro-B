#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 8 (File)

'''Sebuah restoran baru belum memiliki aplikasi kasir sehingga restoran tersebut membutuhkan program sederhana yang digunakan untuk membuat bill pesanan yang dipesan oleh 
pelanggannya. Restoran tersebut ingin mendata bill tersebut sehingga outputnya harus bisa disimpan. Restoran tersebut meminta tolong untuk di buatkan
program untuk kasirnya.

input : - menu yang akan dipilih (dilakukan)
- jumlah jenis menu yang akan di pesan
- jenis menu
- jumlah menu yang akan di pesan
- harga
proses :
- menampung semua dalam variabel-variabel
- melakukan write (ke notepad)
output :
- menampilkan menu, jumlah pesanan, harga
- total semua harga yang dipesan

'''

#Code

print("===== SELAMAT DATANG DI PROGRAM KASIR =====")
print(""" Pilih menu
1. Pesanan baru
2. Tambah pesanan
3. Total pesanan """)
totHarga = 0 
simpan = ""
while True :
    menu = int(input("Pilih menu yang ingin anda jalankan : "))
    if menu == 1:
        bill = open('bill.txt','w')
        jumlah = int(input("Jenis menu yang ingin dipesan : "))
        for i in range (jumlah):
            menu = input("Masukan menu : ")
            jumlahpesan = int(input("Masukan jumlah pesanan : "))
            harga = int(input("Masukan harga : "))
            totHarga += harga*jumlahpesan
            if len(menu)> 14 :
                hasil = "Menu" + '\t'*4 + "Jumlah" + '\t'*2 + "Total\n"
                simpan += hasil + str(menu) + '\t '*2 + str(jumlah) + '\t '*2 + str(harga*jumlahpesan) + '\n'
            elif len(menu) > 7 :
                hasil = "Menu" + '\t'*3 + "Jumlah" + '\t'*3 + "Total\n"
                simpan += hasil + str(menu) + '\t  '*2 + str(jumlah) + '\t'*3 + str(harga*jumlahpesan) + '\n'
            else :
                hasil = "Menu" + '\t'*3 + "Jumlah" + '\t'*3 + "Total\n"
                simpan += hasil + str(menu) + '\t   '*3 + str(jumlah) + '\t'*3 + str(harga*jumlahpesan) + '\n'
    elif menu ==2 :
        bill = open('bill.txt','a')
        jumlah = int(input("Jenis menu yang ingin dipesan : "))
        for i in range (jumlah):
            menu = input("Masukan menu : ")
            jumlahpesan = int(input("Masukan jumlah pesanan : "))
            harga = int(input("Masukan harga : "))
            totHarga += harga*jumlahpesan
            if len(menu)> 14 :
                hasil = "Menu" + '\t'*4 + "Jumlah" + '\t'*2 + "Total\n"
                simpan += hasil + str(menu) + '\t '*2 + str(jumlah) + '\t '*2 + str(harga*jumlahpesan) + '\n'
            elif len(menu) > 7 :
                hasil = "Menu" + '\t'*3 + "Jumlah" + '\t'*3 + "Total\n"
                simpan += hasil + str(menu) + '\t  '*2 + str(jumlah) + '\t'*3 + str(harga*jumlahpesan) + '\n'
            else :
                hasil = "Menu" + '\t'*3 + "Jumlah" + '\t'*3 + "Total\n"
                simpan += hasil + str(menu) + '\t   '*3 + str(jumlah) + '\t'*3 + str(harga*jumlahpesan) + '\n'
    elif menu == 3:
        bill = open('bill.txt','a')
        simpan += '\n'*2 + "Total harga = " + '\t'*3 + str(totHarga)
        bill.write(simpan)
        break
    else :
        print("Invalid input")
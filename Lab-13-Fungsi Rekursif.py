#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 13 (Fungsi Rekursif)

"""Pak Pono memiliki anak yang masih berusia 4 tahun dan ia ingin mengajari anaknya tentang bilangan ganjil dan genap. Ia ingin dibuatkan program namun komputer yang
dimiliki Pak Pono tidak bisa menjalankan program yang berat sehingga dia ingin dibuatkan program yang ringan.

input :

proses :

output :

"""
def ganjil(n=1,simpan=[]):
    if len(simpan) == x:
        return simpan
    else :
        if n % 2 != 0:
            simpan.append(n)
            return ganjil(n+2,simpan)
        else :
            return ganjil(n+1,simpan)
        
def genap(n=1,simpan=[]):
    if len(simpan) == x:
        return simpan
    else :
        if n % 2 == 0:
            simpan.append(n)
            return genap(n+2,simpan)
        else :
            return genap(n+1,simpan)
        
print("""=== Selamat datang di program ganjil genap dengan fungsi rekursif ===
1. Bilangan genap
2. Bilangan ganjil
""")

menu = int(input("Silahkan pilih menu yang ingin anda gunakan : "))
if menu == 1:
    x= int(input("Masukan banyak bilangan genap yang ingin ditampilkan : "))
    print(genap(n=1,simpan=[]))
elif menu == 2 :
    x= int(input("Masukan banyak bilangan ganjil yang ingin ditampilkan : "))
    print(ganjil(n=1,simpan=[]))
else :
    print("Silahkan masukan angka sesuai menu!")
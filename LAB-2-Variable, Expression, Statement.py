# Richardo Chandra Hartono
# 71200642
# Universitas Kristen Duta Wacana
# Pertemuan 2 (Variable - Expression - Statement)

# Masalah
'''Seorang mahasiswa bernama Dedi ingin meringankan beban orang tua dengan mencoba untuk berinvestasi saham,
Dedi membeli saham Widodo Makmur Unggas (WMUU) dengan harga Rp 340 sebanyak 15 lot. Beberapa hari setelah membeli Dedi mengecek kembali harga saham WMUU dan ternyata mengalami
penurunan harga sebanyak 20.56 %. Dedi ingin menghitung jumlah kerugian yang ia peroleh pada saham WMUU

input = 
-nama saham (kode)
-harga beli saham
-jumlah lot yang di beli
-naik/turun (+/-)

proses =
- total uang yang digunakan untuk membeli saham
- keuntungan / kerugian yang di peroleh

output =
- saham wmuu anda mengalami kerugian sebesar = .....
'''

#Code
nama = str(input("Kode saham = "))
harga = int(input("Harga beli saham = Rp "))
lot = int(input("Jumlah lot = "))

total = harga*lot*100
print(f"Total uang yang digunakan untuk membeli saham {nama} = Rp {total}")

print("MENGHITUNG KEUNTUNGAN / KERUGIAN")
perubahan = input("Harga saham mengalami kenaikan atau penurunan? (+/-)")

if perubahan == "+" : 
    naik = float(input("Persen kenaikan harga saham (dalam %) = "))
    total1 = total*naik/100
    print(f"Saham {nama} anda mengalami keuntungan = Rp {total1}")
elif perubahan == "-" :
    turun = float(input("Persen penurunan harga saham (dalam %) = "))
    total2 = total*turun/100
    print(f"Saham {nama} anda mengalami kerugian = Rp {total2}")
else :
    print("salah input")

print("Terimakasih")



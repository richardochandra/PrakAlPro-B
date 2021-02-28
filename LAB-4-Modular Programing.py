# Richardo Chandra H
# 71200642
# Universitas Kristen Duta Wacana 
# Pertemuan 4 ( Modular Programming )

""" Pak Roni mendapat pekerjaan baru yang sangat sensitif dengan waktu sehingga dia harus benar-benar melakukan hal yang diperintahkan oleh atasannya di waktu yang
sudah di tentukan oleh atasannya. Pak Roni merasa terlalu ribet jika dia harus membuka kalkulator untuk mengkonversi dari satuan waktu ke satuan waktu yang lain sehingga
ia meminta untuk dibuatkan program kalkulator konversi waktu dengan batasan jam, menit, dan detik 

input : 
- memilih konversi waktu
- jumlah waktu

proses :
- menghitung waktu
-menampung pada suatu variabel

output :
- hasil dari konversi waktu

"""

#Code

def jam_menit(jam):
    menit = jam *60
    return menit
def menit_detik(menit):
    detik = menit*60
    return detik
def detik_menit(detik):
    menit = detik/60
    return menit
def menit_jam(menit):
    jam = menit/60
    return jam
def jam_detik(jam):
    detik = (jam*60)*60
    return detik
def detik_jam(detik):
    jam = (detik/60)/60
    return jam

print("=== Selamat datang pada program kalkulator konversi waktu ===")
print("""Apa konversi waktu yang ingin anda gunakan?
1. Jam   ke menit
2. Menit ke detik
3. Jam   ke detik
4. Detik ke menit
5. Menit ke jam
6. Detik ke jam
 """)

try :
    jenis = int(input("Masukan pilihan konversi (hanya angka) : "))
    if jenis == 1 :
        jam = float(input("Masukan jam yang ingin anda konversi ke menit = "))
        print(f"Jam yang anda masukan menjadi {jam_menit(jam)} menit")
    elif jenis == 2 :
        menit = float(input("Masukan menit yang anda ingin konversi ke detik = "))
        print(f"Menit yang anda masukan menjadi {menit_detik(menit)} detik")
    elif jenis == 3 :
        jam = float(input("Masukan jam yang ingin anda konversi ke detik = "))
        print(f"Jam yang anda masukan menjadi {jam_detik(jam)} detik")
    elif jenis == 4 :
        detik = int(input("Masukan detik yang anda ingin konversi ke menit = "))
        print(f"Detik yang anda masukan menjadi {detik_menit(detik)} menit")
    elif jenis == 5 :
        menit = float(input("Masukan menit yang anda ingin konversi ke jam = "))
        print(f"Menit yang anda masukan menjadi {menit_jam(menit)} jam")
    elif jenis == 6 :
        detik = int(input("Masukan detik yang anda ingin konversi ke jam = "))
        print(f"Detik yang anda masukan menjadi {detik_jam(detik)} jam")
    else :
        print("Input yang anda masukan salah")
except :
    print("Input yang anda masukan tidak valid")
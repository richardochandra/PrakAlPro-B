# Richardo Chandra H
# Universitas Kristen Duta Wacana 
# 71200642
# Struktur Kontrol Perulangan

""" RS ABC sedang kesulitan melakukan pendataan sementara untuk pasien covid dan jumlah pasien yang meninggal atau sembuh. RS ABC
menginginkan program untuk pendataan pasien yang menampilkan jumlah-jumlahnya dan persentase perbagiannya

input :
masuk/keluar
covid/bukan
sembuh/meninggal

proses :
menambahkan tiap pasien ke variabel yang telah kita definisikan di awal
menghitung persentase tiap-tiap keadaan

output : 
menampilkan jumlah pasien tiap-tiap keadaan
persentase pasien tiap keadaan

"""
#coding

print("PENDATAAN PASIEN COVID-19")
pasCovid = 0
pasLain = 0
jumTot = 0
jumMeninggal = 0
jumSembuh = 0 

while True :
    masuk = str(input("masuk/keluar :")).lower()
    if masuk == "masuk" :
        nama = str(input("Masukan nama : "))
        print("berhasil di input")
        print()
        covid = str(input("covid/lainnya : ")).lower()
        if covid == "covid":
            pasCovid +=1
            jumTot +=1
            print("Berhasil ditambahkan ke pasien COVID \n")
            keadaan = str(input("meninggal/sembuh : ")).lower()
            if keadaan =="meninggal":
                jumMeninggal += 1
                print("Berhasil diinput")
            elif keadaan =="sembuh":
                jumSembuh +=1
                print("berhasil diinput")
        elif covid == "lainnya":
            pasLain +=1
            jumTot +=1
            print("berhasil di tambahkan ke pasien lainnya")
    elif masuk == "keluar" :
        break
print(f"Jumlah pasien covid = {pasCovid}")
print(f"Jumlah pasien lainnya = {pasLain}")
print(f"Jumlah pasien covid yang meninggal = {jumMeninggal}")
print(f"Jumlah pasien covid yang sembuh = {jumSembuh}")
print(f"Jumlah pasien seluruhnya = {jumTot}")

persen = str(input("apakah ingin menampilkan persentase (ya/tidak) : ")).lower()
if persen =="ya":
    print(f"Persentase pasien covid = {(pasCovid/jumTot)*100} %")
    print(f"Persentase pasien lainnya = {(pasLain/jumTot)*100} %")
    print(f"Persentase pasien covid yang meninggal = {(jumMeninggal/pasCovid)*100} %")
    print(f"Persentase pasien covid yang sembuh = {(jumSembuh/pasCovid)*100} %")
    print("program telah selesai")
elif persen == "tidak":
    print("program telah selesai")

print("terimakasih")
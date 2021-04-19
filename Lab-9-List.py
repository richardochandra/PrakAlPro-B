#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 9 (List)

""" Pak Roro adalah seorang guru matematika SMA, ia ingin dibuatkan program untuk
mengecek hasil ujian dari murid-muridnya yang materinya adalah himpunan. Ia ingin
program yang menampilkan gabungan, irisan, dan menyatukan himpunan.
Buatkan program untuk Pak Roro 

input : 
- himpunan A
- himpunan B
- proses yang ditampilkan (gabungan, irisan, atau menyatukan)

proses : 
- memasukan angka kedalam list
- mengecek angka yang ada dalam list kemudian dimasukan ke list baru sesuai dengan kebutuhan (proses yang diinginkan)

output : 
- list baru yang berupa hasil dari proses diatas (gabungan, irisan, atau menyatukan)

"""

#CODE 

himp1 = []
himp2 = []

while True:
    input1 = int(input("Silahkan masukan angka untuk himpunan pertama (-999 untuk lanjut) : "))
    himp1.append((input1))
    if input1 == -999:
        himp1.remove(-999)
        while True :
            input2 = int(input("Silahkan masukan angka untuk himpunan kedua (-999 untuk lanjut) : "))
            himp2.append(input2)
            if input2 == -999:
                himp2.remove(-999)
                break
        break

himp1.sort()
himp2.sort()

print(himp1)
print(himp2)

print("""
1. Gabungan (Union)
2. Irisan 
3. Menyatukan """)

while True:
    menu = int(input("Masukan pilihan menu : "))
    himp3=[]
    if menu == 1 :
        for i in (himp1):
            if i not in himp3 :
                himp3.append(i)
        for i in (himp2):
            if i not in himp3:
                himp3.append(i)
        himp3.sort()
        print(f"Gabungan dari himpunan pertama dan himpunan kedua adalah {himp3}")
    elif menu == 2:
        if himp1>himp2 :
            for i in (himp1):
                if i in (himp2) and i not in himp3:
                    himp3.append(i)
        elif himp2 >= himp1 :
            for i in (himp2):
                if i in himp1 and i not in himp3:
                    himp3.append(i)
        himp3.sort()
        print(f"Irisan dari himpunan pertama dan kedua adalah {himp3}")
    elif menu == 3:
        for i in himp1:
            himp3.append(i)
        for i in himp2:
            himp3.append(i)
        himp3.sort()
        print(f"Hasil dari menyatukan himpunan pertama dan kedua adalah {himp3}")
    lanjut = int(input("Masukan angka 1 untuk lanjut : "))
    if lanjut == 1 :
        continue
    else :
        break
    
print("Terimakasih sudah menggunakan program ini. Semoga bermanfaat")


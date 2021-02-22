# Richardo Chandra H
# 71200642
# Universitas Kristen Duta Wacana 
# Pertemuan 3 ( Struktur Kontrol Percabangan )

# Masalah
""" 
Wasino adalah seorang ayah yang memiliki anak bernama Budi, Budi adalah anak 
yang kurang pandai dalam matematika terutama tambah, kurang, kali, dan bagi sehingga 
Wasino meminta tolong untuk dibuatkan program game sederhana tentang matematika untuk membantu anaknya belajar.

input = 
- input operator
- jawaban 

proses = 
- soal berdasarkan operator 
- menampung jawaban dari soal

output = 
"SELAMAT JAWABAN ANDA BENAR!"
"JANGAN MENYERAH DAN COBA LAGI!"
"""

#Code 

import random as random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,9)
d = random.randint(1,9)

print("======== Selamat datang di game matematika sederhana =========")
print(""" 
1. Tambah (+)
2. Kurang (-)
3. Kali (x)
4. Bagi (/)
""")

try :
    x = int(input("Silahkan pilih materi permainan anda (hanya angka) : "))
    if x == 1 :
        print(f"Berapa hasil dari {a} + {b} ?")
        hasil = a+b
        jawab = int(input("Jawab = "))
        if hasil == jawab :
            print("SELAMAT JAWABAN ANDA BENAR!")
        elif hasil != jawab :
            print("JANGAN MENYERAH DAN COBA LAGI!")
            print(f"Jawaban yang benar adalah {hasil}")
    elif x == 2 :
        print(f"Berapa hasil dari {a} - {b} ?")
        hasil = a-b
        jawab = int(input("Jawab = "))
        if hasil == jawab :
            print("SELAMAT JAWABAN ANDA BENAR!")
        elif hasil != jawab :
            print("JANGAN MENYERAH DAN COBA LAGI!")
            print(f"Jawaban yang benar adalah {hasil}")
    elif x == 3 :
        print(f"Berapa hasil dari {c} x {d}?")
        hasil = c*d
        jawab = int(input("Jawab = "))
        if hasil == jawab :
            print("SELAMAT JAWABAN ANDA BENAR!")
        elif hasil != jawab :
            print("JANGAN MENYERAH DAN COBA LAGI!")
            print(f"Jawaban yang benar adalah {hasil}")
    elif x == 4 :
        print(f"Berapa hasil dari {c} / {d}?")
        hasil = c/d
        hasil = round(hasil,1)
        jawab = float(input("Jawab (satu angka dibelakang koma jika jawabanya pecahan)= "))
        if hasil == jawab :
            print("SELAMAT JAWABAN ANDA BENAR!")
        elif hasil != jawab :
            print("JANGAN MENYERAH DAN COBA LAGI!")
            print(f"Jawaban yang benar adalah {hasil}")
    else :
        print("Salah input")
except :
    print("Input yang anda masukan tidak valid")



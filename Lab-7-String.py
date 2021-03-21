#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 7 (String)

"""Pak Odading memiliki seorang anak yang hobi bermain dengan kata/huruf sehingga ia berinisiatif
untuk membuat sebuah program yang bermain dengan kata. Program yang Pak Odading inginkan adalah 
program yang bisa mengganti suatu huruf/kata menjadi huruf atau kata yang diinginkannya. 
Pak Odading meminta untuk dibuatkan program tersebut.

input :
-kalimat yang ingin diubah-ubah
-huruf/kata dalam kalimat yang ingin di ganti 
-huruf/kata pengganti

proses :
-pengecekan apakah huruf/kata ada dalam kalimat tersebut kemudian jika ada maka akan 
diganti dengan huruf/kata pengganti 

output :
-kalimat yang huruf/katanya sudah terganti oleh huruf/kata pengganti

"""

#CODING
print("PROGRAM INI CASESENSITIVE")
kalimat = input("Masukan kalimat : ")
jenis = input("Anda ingin mengganti kata/huruf : ")
if jenis == "huruf":
    awal = input("Huruf apa yang ingin anda ubah (bisa anda isi dengan vokal untuk mengganti huruf vokal) : ")
    jadi = input("Ingin anda ganti menjadi : ")
    fix = ""
    if awal != "vokal" :
        for i in kalimat :
            if i == awal :
                i = jadi
                fix += i
            else :
                fix += i
        print(f"Anda mengubah '{kalimat}' menjadi '{fix}'")
    elif awal == "vokal":
        aiueo = "AIUEOaiueo"
        for i in kalimat :
            if i in aiueo :
                i = jadi
                fix += i
            else :
                fix +=i
        print(f"Anda mengubah '{kalimat}' menjadi '{fix}'")
elif jenis == "kata":
    pisah = kalimat.split()
    awal = input("Kata yang ingin anda ubah : ")
    jadi = input("Ingin anda ganti menjadi : ")
    fix = ""
    for i in pisah :
        if i == awal :
            i = jadi
            fix +=i + " "
        else :
            fix += i + " "
    print(f"Anda mengubah '{kalimat}' menjadi '{fix[:-1]}'")


#Richardo Chandra H
#71200642
#Universitas Kristen Duta Wacana
#Pertemuan 11 (Tuple)

""" Pak Po memiliki 2 toko, ia ingin melakukan pembandingan pendapatan antara 2 toko tersebut sehingga ia ingin membuat program yang dapat melakukan
penotalan dari pendapatan per toko dari data yang dilaporkan oleh pegawainya. Bantu Pak Po untuk membuat program tersebut

input : 
- pendapatan toko A perhari
- pendapatan toko B perhari

proses :
- menjumlahkan pendapatan perhari dari toko A dan B
- membandingkan besarnya pendapatan

output :
- pendapatan total toko A 
- pendapatan total toko B
- pendapatan toko yang lebih besar

"""

#CODE

def bandingHarga(A,B):
    totalA = 0
    for i in A:
        totalA+= i
    totalB = 0
    for j in B:
        totalB+=j
    
    dA = dict()
    dB = dict()

    dA[A] = totalA
    dB[B] = totalB

    print(f"Toko A : {dA}")
    print(f"Toko B : {dB}")
    print()
    print("Kesimpulannya adalah : ")

    if totalA > totalB :
        print(f"Pendapatan toko A lebih besar dari toko B sejumlah Rp. {totalA-totalB}000")
    elif totalB > totalA:
        print(f"Pendapatan toko B lebih besar dari toko A sejumlah Rp. {totalB-totalA}000")
    else:
        print(f"Jumlah pendapatan toko A dan toko B adalah sama yaitu sejumlah Rp. {totalA}000")

# MASUKAN DALAM SATUAN RIBUAN RUPIAH  
A = (100,140,130,50,80,40,250,300,500,500)
B = (200,50,130,100,60,50,100,200,500,400)

bandingHarga(A,B)


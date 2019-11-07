def insertionSort(listsaya):
    for index in range(1, len(listsaya)):
        posisiKanan = listsaya[index]
        posisiKiri = index - 1
        while posisiKiri >=0 and listsaya[posisiKiri] > posisiKanan:
            listsaya[posisiKiri + 1] = listsaya[posisiKiri]
            posisiKiri -= 1
        listsaya[posisiKiri + 1] = posisiKanan

index = 0
panjangList = int(input("Jumlah orang = "))
listsaya=[]
for i in range(1,panjangList+1):
    angka = int(input("Tujuan orang ke %i Menuju Lantai = " %i))
    listsaya.append(angka)
posisilantai = int(input("posisi lantai sekarang = "))

result = filter(lambda x: x < posisilantai, listsaya)
print("Lift Bergerak Turun Ke = ")
print(list(result))
result = filter(lambda x: x > posisilantai, listsaya)
print("Lift Bergerak Naik Ke = ")
print(list(result))
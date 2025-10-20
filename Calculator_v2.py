#Operator Aritmatika
'''nilai_1 = int(input('Masukkan Nilai Pertama : '))
nilai_2 = int(input('Masukkan Nilai Kedua : '))
penjumlahan = nilai_1 + nilai_2
print(nilai_1, "+", nilai_2, "=", penjumlahan)
pengurangan = nilai_1 - nilai_2
print(nilai_1, "-", nilai_2, "=", pengurangan)
perkalian = nilai_1 * nilai_2
print(nilai_1, "x", nilai_2, "=", perkalian)
pembagian = nilai_1 / nilai_2
print(nilai_1, "/", nilai_2, "=", pembagian)
pemangkatan = nilai_1 ** nilai_2
print(nilai_1, "**", nilai_2, "=", pemangkatan)
pembagian_bulat = nilai_1 // nilai_2
print(nilai_1, "//", nilai_2, "=", pembagian_bulat)'''

#Operator Perbandingan
'''n1 = int(input('Nilai 1: '))
n2 = int(input('Nilai 2: '))

print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)
print(n1 == n2)
print(n1 != n2)'''

#Operator Penugasan
#Operator Logika
#Operator Bitwise
print(bin(7))
print(bin(1))
print(5 | 3)
print(5 & 3)
#Operator Indentitas
a = 10
b = 5
c = a > b
if c is True:
    print('Nilai a lebih dari Nilai b')
else:
    print('Nilai a tidak lebih dari Nilai b')

if c is not True:
    print('nilai a lebih dari b')
else:
    print('nilai a tidak lebih dari nilai b')
#Operator Keanggotaan
a = [10, 20, 21, 4, 1, 100]

if 21 in a:
    print('21 ada didalam a')
else:
    print('21 tidak ada didalam a')
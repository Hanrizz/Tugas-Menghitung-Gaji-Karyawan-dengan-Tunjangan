print('##  PROGRAM PYTHON KALKULATOR SEDERHANA  ##')
print('===========================================')
print()

print('1. Penjumlahan')
print('2. pengurangan')
print('3. Perkalian')
print('4. pembagian')
print('5. Modulus')
print()

pilihan = int(input('Input pilihan operasi: '))
num = float(input('Angka Pertama: '))
num2 = float(input('Angka Kedua: '))
print

if pilihan == 1:
    print('Hasil dari', num, '+', num2, '=', round(num + num2, 2))
elif pilihan == 2:
    print('Hasil dari', num, '-', num2, '=', round(num - num2, 2))
elif pilihan ==3:
    print('Hasil dari'), num, '*', num2, '=', round(num * num2, 2)
elif pilihan == 4:
    print('Hasil dari', num, '/', num2, '=', round(num / num2, 2))
elif pilihan == 5:
    print('Hasil dari', num, '%', num2, '=', round(num % num2, 2))
else:
    print('Maaf, piliha menu tidak tersedia')
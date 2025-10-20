nilai = int(input('Masukkan Nilai Anda: '))
if nilai >= 80 and nilai <=100:
    huruf = 'A (Nilai Sempurna)'
elif nilai >=70 and nilai <=79:
    huruf = 'B (Nilai Bagus)'
elif nilai >=60 and nilai <=69:
    huruf = 'C (Cukup Bagus)'
elif nilai >= 31 and nilai <=59:
    huruf = 'D (Dungu)'
elif nilai >= 0 and nilai <= 30:
    huruf = 'E (Eladalah)'
else:
    huruf = 'Tidak Ternilai'

print('Nilai Anda: ', nilai)
print('Predikat Anda: ', huruf)
'''Nilai = int(input('Masukan Nilai Anda: '))
if Nilai >= 70:
    print('Selamat Anda Lulus')
print('Silahkan lanjut ujian berikutnya')'''


'''Nilai = int(input('Masukkan Nilai Anda: '))
if Nilai >= 80:
    print('Selamat Anda Lulus dengan predikat A')
else:
    print('Anda Tidak Lulus')'''


'''Nilai = int(input('Masukkan Nilai Anda: '))
if Nilai >= 90:
    print('Selamat Anda Mendapat Nilai A')
elif Nilai >= 70:
    print('Selamat Anda Mendapat Nilai B')
elif Nilai >= 50:
    print('Selamat Anda Mendapat Nilai C')
else:
    print('Anda GAGAL')'''


#Studi Kasus 4
'''print('===PROGRAM PENGHITUNG GAJI KARYAWAN===')
gaji_pokok = 5000000
jumlah_produk = int(input('Masukkan Jumlah Produk yang Terjual: '))
harga_satuan_produk = float(input('Masukkan Harga Produk: '))
omset = jumlah_produk * harga_satuan_produk
if jumlah_produk >= 100:
    bonus = 0.20 * gaji_pokok
else:
    bonus = 0.10 * gaji_pokok
gaji_total = gaji_pokok + bonus

print('================================')
print('Gaji Pokok Anda: Rp', gaji_pokok)
print('Omset Penjualan Anda: Rp', omset)
print('Bonus Anda: Rp', bonus)
print('Gaji Total Anda: Rp', gaji_total)'''


#Studi kasus 5
print('===PROGRAM PENGHITUNG GAJI KARYAWAN===')

gaji_pokok = float(input('Masukkan Gaji Pokok Anda: Rp '))
jam_kerja = int(input('Masukkan Jumlah Jam Kerja Anda: '))

tunjangan = 0.20 * gaji_pokok
lembur = 0
if jam_kerja > 200:
    kelebihan_jam = jam_kerja - 200
    lembur = kelebihan_jam * 20000

gaji_kotor = gaji_pokok + tunjangan + lembur

pajak = 0.10 * gaji_kotor
gaji_bersih = gaji_kotor - pajak

print('\n=======================================')
print(f'Gaji Pokok      : Rp {gaji_pokok:,.2f}')
print(f'Tunjangan (20%) : Rp {tunjangan:,.2f}')
print(f'Lembur          : Rp {lembur:,.2f}')
print(f'Gaji kotor      : Rp {gaji_kotor:,.2f}')
print(f'Pajak (10%)     : Rp {pajak:,.2f}')
print('='*30)
print(f'GAJI BERSIH     : Rp {gaji_bersih:,.2f}')
#LA

#DP
'''angka = 5
if angka > 0:
    print(angka, "adalah bilangan positif")

angka = -1
#yang berikut akan bernilai false sehingga tidak diesekusi
if angka > 0:
    print(angka, 'adalah bilangan negatif')'''

'''kode_baju = input("Masukkan Kode Baju [SP/AD] : ")
ukuran = input('Masukkan Ukuran Baju [S/M] : ')

if kode_baju == 'SP' or kode_baju == 'sp' :
    merk = 'SuperDry'
    if ukuran=='S' or ukuran == 's':
        harga = 450000
    elif ukuran=='M' or ukuran == 'm':
        harga = 500000
    else:
        harga = 0
elif kode_baju == 'AD' or kode_baju == 'ad' :
    merk = 'Adidas'
    if ukuran=='S' or ukuran == 's' :
        harga = 650000
    elif ukuran=='M' or ukuran == 'm' :
        harga = 700000
    else:
        harga = 0

else:
    merk = 'Anda Salah Input Kode Merk'
    harga = 0

print('...............................................')
print('Merk Baju : '+str(merk))
print(f'Harga Baju : Rp. {harga:,.0f}')'''
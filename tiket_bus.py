#input
pembeli = input('Input Nama Pembeli : ')
no_hp = input('Input No. Handphone : ')
jurusan = input('Input Jurusan [SBY/BL/LMP] : ')

#proses
if jurusan == 'SBY':
    namajurusan = 'Surabaya'
    harga = 300000
elif jurusan == 'BL':
    namajurusan = 'Bali'
    harga = 350000
else:
    namajurusan = 'Lampung'
    harga = 500000

#input Jumlah Beli
jumlah = int(input('Masukkan Jumlah Beli : '))

#proses potongan
if jumlah>=3 :
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0
total = (jumlah * harga)- potongan

#cetak hasil
print('--------------------------------------------------------')
print('                  PENJUALAN TIKET BUS                   ')
print('                             XYZ')
print('--------------------------------------------------------')
print('Nama Pembeli    :'+str(pembeli))
print('No. Handphone   :'+ str(no_hp))
print('Kode Jurusan yang dipilih : '+ str(jurusan))
print('Nama Kota Jurusan :'+ str(namajurusan))
print('Harga           :' +str(harga))
print('Jumlah Beli     :' +str(jumlah))
print('--------------------------------------------------------')
print('potongan yang didapat :' +str(potongan))
print('Total Bayar     :' +str(total))
ubay = int(input('Masukkan Uang Bayar : '))
uangkembali = ubay - total
print('Uang Kembali    :' +str(uangkembali))
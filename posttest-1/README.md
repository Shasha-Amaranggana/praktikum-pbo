# Posttest 2 - Sistem Penjualan dan Pemesanan Merchandise Genshin Impact pada Platform Toko Online


═════════════════════════════════════════════════════════════════════════════════════════════


## Deskripsi Program

Program yang mensimulasikan sistem penjualan dan pemesanan merchandise Genshin Impact lewat Online.

Program ini menerapkan konsep OOP, seperti class, object, attribute, method, encapsulation dan property. Tersedia juga fitur untuk menyimpan data merchandise, pengguna, dan pesanan.

Program dapat melakukan beberapa proses, yaitu:

> Menambahkan dan menampilkan data merchandise.
> Menghitung diskon merchandise.
> Mengurangi stok merchandise setelah pembelian.
> Menambahkan dan menampilkan data user.
> Melakukan login user.
> Melakukan pembelian merchandise.
> Mengubah password sesuai ketentuan.
> Mengurangi saldo user setelah pembelian.
> Menambahkan dan menampilkan data pesanan.
> Mengirim pesanan.
> Menghitung total seluruh pesanan.
> Mengubah status pesanan.
> Menguji getter dan setter yang ada.


═════════════════════════════════════════════════════════════════════════════════════════════


## Struktur Class
Program terdiri dari tiga class utama, yaitu:


### 1. Class `merchandise`
Digunakan untuk menyimpan data merchandise yang tersedia.

#### Class Attribute
- `totalMerchandise` = Menyimpan jumlah seluruh objek merchandise yang dibuat.

#### Instance Attribute
- `nama` = Menyimpan nama merchandise.
- `harga` = Menyimpan harga merchandise.
- `__stok` = Menyimpan jumlah stok merchandise secara private.

#### Method
- `__init__()` = Membuat objek merchandise dan mengisi data awal.
- `tampilkanInfo()` = Menampilkan informasi merchandise.
- `hitungDiskon()` = Menghitung harga setelah diskon.
- `property stok` = Getter untuk mengambil nilai stok.
- `stok.setter` = Mengubah stok dengan validasi agar tidak boleh negatif.

___________________________________________

### 2. Class `user`
Digunakan untuk menyimpan data pengguna..

#### Class Attribute
- `totalUser` = Menyimpan jumlah seluruh objek user yang dibuat.
- `statusUser` = Menyimpan status default user.

#### Instance Attribute
- `username` = Menyimpan username user.
- `email` = Menyimpan email user.
- `alamat` = Menyimpan alamat user.
- `__password` = Menyimpan password user secara private.
- `__saldo` = Menyimpan saldo user secara private.

#### Method
- `__init__()` = Membuat objek user dan mengisi data awal.
- `login()` = Melakukan pengecekan username dan password.
- `pembelian()` = Melakukan proses pembelian merchandise.
- `property saldo` = Getter untuk mengambil nilai saldo.
- `saldo.setter` = Mengubah saldo dengan validasi agar tidak boleh negatif.
- `property password` = Getter untuk mengambil password.
- `password.setter` = Mengubah password dengan validasi agar tidak boleh kosong.

___________________________________________

### 3. Class `pesanan`
Digunakan untuk menyimpan data pesanan yang dilakukan oleh user.

#### Class Attribute
- `statusDefault` = Menyimpan status awal pesanan.
- `totalPesanan` = Menyimpan jumlah seluruh pesanan yang dibuat.
- `daftarPesanan` = Menyimpan seluruh objek pesanan.

#### Instance Attribute
- `user` = Menyimpan user yang melakukan pesanan.
- `merchandise` = Menyimpan merchandise yang dipesan.
- `__jumlah` = Menyimpan jumlah merchandise yang dipesan secara private.
- `__status` = Menyimpan status pesanan secara private.

#### Method
- `__init__()` = Membuat objek pesanan dan memasukkannya ke dalam `daftarPesanan`.
- `tampilkanPesanan()` = Menampilkan informasi pesanan.
- `kirimPesanan()` = Mengubah status pesanan menjadi "Dikirim".
- `totalSemuaPesanan()` = Menghitung total harga dari seluruh pesanan.
- `property jumlah` = Getter untuk mengambil jumlah pesanan.
- `jumlah.setter` = Mengubah jumlah pesanan dengan validasi.
- `property status` = Getter untuk mengambil status pesanan.
- `status.setter` = Mengubah status pesanan dengan validasi agar tidak boleh kosong.


═════════════════════════════════════════════════════════════════════════════════════════════


## Panduan Menjalankan Program


### 1. Buka folder `posttest2`
Buka folder `posttest2` menggunakan Visual Studio Code.

### 2. Jalankan program
Buka terminal pada folder tersebut, kemudian jalankan file "posttest_2509106063_DindaShashaAmaranggana"

### 3. Amati output program
Program akan menampilkan beberapa bagian pengujian, yaitu:

1. Pengujian `tampilkanInfo()`.
3. Pengujian `hitungDiskon()`.
4. Data user.
5. Pengujian `login`.
6. Pengujian `pembelian`.
7. Pengujian `tampilkanPesanan()`.
9. Pengujian `totalSemuaPesanan()`.
10. Pengujian `kirimPesanan()`.
11. Pengujian setter valid.
12. Pengujian setter tidak valid.
13. Total merchandise, pesanan, dan user.


═════════════════════════════════════════════════════════════════════════════════════════════


## Panduan Pengujian


### 1. Pengujian Instance Method
Instance method diuji dengan seperti:

```python
merch1.tampilkanInfo()
user1.login("ayak", "12345")
pesan1.tampilkanPesanan()
pesan1.kirimPesanan()
```

Pengujian dilakukan dengan melihat hasil yang ditampilkan pada terminal.

### 2. Pengujian Static Method
Static method diuji dengan seperti:

```python
merchandise.hitungDiskon(merch1.harga, 10)
```

Pengujian ini digunakan untuk memastikan harga setelah diskon dapat dihitung dengan benar.

### 3. Pengujian Class Method
Class method diuji dengan seperti:

```python
pesanan.totalSemuaPesanan()
```

Method ini digunakan untuk menghitung total harga dari seluruh pesanan yang telah dibuat.

### 4. Pengujian Setter Valid
Setter diuji dengan data yang valid seperti:

```python
merch1.stok = 5
user1.saldo = 400000
user1.password = "54321"
pesan1.jumlah = 3
pesan1.status = "Diproses"
```

Data berhasil diubah karena memenuhi aturan validasi.

### 5. Pengujian Setter Tidak Valid
Setter juga diuji dengan data yang tidak valid seperti:

```python
merch1.stok = -5
user1.saldo = -100000
user1.password = ""
pesan1.jumlah = 0
pesan1.status = ""
```

Program menggunakan `try-except` untuk menangkap `ValueError` dan menampilkan pesan kesalahan.


═════════════════════════════════════════════════════════════════════════════════════════════


## Kesimpulan

Program ini menerapkan konsep dasar OOP melalui tiga class, yaitu `merchandise`, `user`, dan `pesanan`.

Konsep yang diterapkan meliputi class, object, attribute, method, encapsulation dan property. Program juga menyediakan pengujian terhadap semua method dan setter menggunakan data valid maupun tidak valid.
# CLASS MERCHANDISE
# ============================
class merchandise:
    totalMerchandise = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.__stok = stok
        merchandise.totalMerchandise += 1

    def tampilkanInfo(self):
        print("Nama Merchandise  :", self.nama)
        print(f"Harga             : Rp{self.harga}")
        print("Stok              :", self.__stok)

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif.")
        self.__stok = stok

    @staticmethod
    def hitungDiskon(harga, persen):
        return harga - (harga * persen / 100)

# CLASS PESANAN
# ============================
class pesanan:
    statusPesanan = "Menunggu Pembayaran"
    totalPesanan = 0
    daftarPesanan = []

    def __init__(self, user, merchandise, jumlah):
        self.user = user
        self.merchandise = merchandise
        self.__jumlah = jumlah
        self.__status = pesanan.statusDefault
        pesanan.totalPesanan += 1
        pesanan.daftarPesanan.append(self)

    def tampilkanPesanan(self):
        print("User       :", self.user.username)
        print("Merchandise:", self.merchandise.nama)
        print("Jumlah     :", self.__jumlah)
        print("Total Harga:", self.merchandise.harga * self.__jumlah)
        print("Status     :", self.__status)

    def kirimPesanan(self):
        self.__status = "Dikirim"
        print("Pesanan telah dikirim kepada", self.user.username)

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pesanan harus lebih dari 0.")
        self.__jumlah = jumlah

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status == "":
            raise ValueError("Status tidak boleh kosong.")
        self.__status = status

    @classmethod
    def totalSemuaPesanan(cls):
        total = 0
        for pesanan in cls.daftarPesanan:
            total += pesanan.merchandise.harga * pesanan.jumlah
        return total


# CLASS USER
# ============================
class user:
    totalUser = 0
    statusUser = "Aktif"

    def __init__(self, username, password, email, alamat, saldo):
        self.username = username
        self.email = email
        self.alamat = alamat
        self.__password = password
        self.__saldo = saldo
        user.totalUser += 1

    def login(self, username, password):
        if self.username == username and self.__password == password:
            return True
        else:
            return False

    def pembelian(self, merchandise, jumlah):
        total = merchandise.harga * jumlah
        if self.__saldo >= total and merchandise.stok >= jumlah:
            self.__saldo -= total
            merchandise.stok -= jumlah
            return True
        else:
            return False

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif.")
        self.__saldo = saldo

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password == "":
            raise ValueError("Password tidak boleh kosong.")
        self.__password = password


# MAIN PROGRAM
# ============================
print("══════════════ 「 DATA MERCHANDISE 」 ══════════════\n")


merch1 = merchandise("Flins Acrylic Stand", 150000, 10)
merch2 = merchandise("Alhaitham Keychain", 20000, 20)

print(" 『 INSTANCE METHOD (TAMPILKAN INFO) 』\n")
merch1.tampilkanInfo()
print()
merch2.tampilkanInfo()

print("\n\n 『 STATIC METHOD (HITUNG DISKON) 』\n")
hargaDiskon = merchandise.hitungDiskon(merch1.harga, 10)
print(f"Harga Flins setelah diskon 10%: Rp{hargaDiskon}")



print("\n\n\n══════════════ 「 DATA USER 」 ══════════════\n")


user1 = user("ayak", "12345", "dinda@gmail.com", "Samarinda", 500000)
user2 = user("shashak", "67890", "shasha@gmail.com", "Balikpapan", 300000)
print("Username Ayak :", user1.username)
print("Username Shasha :", user2.username)

print("\n\n 『 INSTANCE METHOD (LOGIN) 』\n")
print("Login Ayak :", user1.login("ayak", "12345"))
print("Login Shasha :", user2.login("shashak", "67890"))

print("\n\n 『 INSTANCE METHOD (PEMBELIAN) 』\n")
if user1.pembelian(merch1, 2):
    print("Pembelian Ayak berhasil.")
    pesan1 = pesanan(user1, merch1, 2)
    print("Saldo Ayak :", f"Rp{user1.saldo}")
    print("Stok Flins   :", merch1.stok)
else:
    print("Pembelian Ayak gagal.")
print()
if user2.pembelian(merch2, 3):
    print("Pembelian Shasha berhasil.")
    pesan2 = pesanan(user2, merch2, 3)
    print("Saldo Shasha :", f"Rp{user2.saldo}")
    print("Stok Alhaitham :", merch2.stok)
else:
    print("Pembelian Shasha gagal.")



print("\n\n\n══════════════ 「 DATA PESANAN 」 ══════════════\n")


print(" 『 INSTANCE METHOD (TAMPILKAN PESANAN) 』\n")
pesan1.tampilkanPesanan()
print()
pesan2.tampilkanPesanan()

print("\n\n 『 CLASS METHOD (TOTAL SEMUA PESANAN) 』\n")
print("Total seluruh pesanan :",
      f"Rp{pesanan.totalSemuaPesanan()}")

print("\n\n 『 INSTANCE METHOD (KIRIM PESANAN) 』\n")
pesan1.kirimPesanan()
print("Status Pesanan 1 :", pesan1.status)



print("\n\n\n══════════════ 「 PENGUJIAN SETTER VALID 」 ══════════════\n")


merch1.stok = 5
print("Stok Flins setelah diubah       :", merch1.stok)

user1.saldo = 400000
print("Saldo Ayak setelah diubah       :", f"Rp{user1.saldo}")

user1.password = "54321"
print("Password Ayak berhasil diubah.")

pesan1.jumlah = 3
print("Jumlah Pesanan 1 setelah diubah :", pesan1.jumlah)

pesan1.status = "Diproses"
print("Status Pesanan 1 setelah diubah :", pesan1.status)



print("\n\n\n══════════════ 「 PENGUJIAN SETTER TIDAK VALID 」 ══════════════\n")


try:
    merch1.stok = -5
except ValueError as e:
    print("Stok tidak valid     :", e)

try:
    user1.saldo = -100000
except ValueError as e:
    print("Saldo tidak valid    :", e)

try:
    user1.password = ""
except ValueError as e:
    print("Password tidak valid :", e)

try:
    pesan1.jumlah = 0
except ValueError as e:
    print("Jumlah tidak valid   :", e)

try:
    pesan1.status = ""
except ValueError as e:
    print("Status tidak valid   :", e)



print("\n\n\n══════════════ 「 TOTAL MERCH, PESANAN, USER 」 ══════════════\n")


print("Total Merchandise :", merchandise.totalMerchandise)
print("Total Pesanan     :", pesanan.totalPesanan)
print("Total User        :", user.totalUser)
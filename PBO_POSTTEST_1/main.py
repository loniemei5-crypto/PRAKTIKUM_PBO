class Barang:

    nama_sistem = "Sistem Pendataan Barang Kos"
    total_barang = 0
    kategori_default = "Barang Kos"

    def __init__(self, kode_barang, nama_barang, stok):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang

        self.__stok = 0

        self.stok = stok

        Barang.total_barang += 1

    def tampilkan_info(self):
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self.stok}")

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah yang ditambahkan harus lebih dari 0.")

        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah yang dikurangi harus lebih dari 0.")

        if jumlah > self.stok:
            raise ValueError("Stok tidak mencukupi.")

        self.stok -= jumlah

    @classmethod
    def ubah_nama_sistem(cls, nama_baru):
        if not nama_baru.strip():
            raise ValueError("Nama sistem tidak boleh kosong.")

        cls.nama_sistem = nama_baru

    @classmethod
    def tampilkan_total_barang(cls):
        print(f"Total objek barang: {cls.total_barang}")

    @staticmethod
    def validasi_nama(nama):
        if not nama.strip():
            return False

        return True

    @staticmethod
    def validasi_kode(kode):
        if not kode.strip():
            return False

        return True

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if not isinstance(nilai, int):
            raise ValueError("Stok harus berupa angka bulat.")

        if nilai < 0:
            raise ValueError("Stok tidak boleh negatif.")

        self.__stok = nilai
##############################################################################
class Kamar:

    nama_sistem = "Sistem Pendataan Barang Kos"
    total_kamar = 0
    tipe_kamar_default = "Kamar Kos"

    def __init__(self, nomor_kamar, nama_kamar):
        # Atribut instance
        self.nomor_kamar = nomor_kamar
        self.nama_kamar = nama_kamar
        self.barang_list = []

        # Menambah jumlah objek Kamar
        Kamar.total_kamar += 1

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    def tampilkan_info(self):
        print(f"Nomor Kamar : {self.nomor_kamar}")
        print(f"Nama Kamar  : {self.nama_kamar}")

        print("Daftar Barang:")

        if len(self.barang_list) == 0:
            print("- Belum ada barang")
        else:
            for barang in self.barang_list:
                print(
                    f"- {barang.nama_barang} "
                    f"(Kode: {barang.kode_barang}, "
                    f"Stok: {barang.stok})"
                )

    @classmethod
    def tampilkan_total_kamar(cls):
        print(f"Total objek kamar: {cls.total_kamar}")

    @staticmethod
    def validasi_nomor_kamar(nomor):
        return str(nomor).strip() != ""

class Penghuni:

    nama_sistem = "Sistem Pendataan Barang Kos"
    total_penghuni = 0
    status_default = "Aktif"

    def __init__(self, nama, nim, kamar):
        # Atribut instance
        self.nama = nama
        self.nim = nim
        self.kamar = kamar

        # Menambah jumlah objek Penghuni
        Penghuni.total_penghuni += 1


    def tampilkan_info(self):
        print(f"Nama Penghuni : {self.nama}")
        print(f"NIM            : {self.nim}")
        print(f"Kamar          : {self.kamar.nomor_kamar}")

    def tampilkan_barang_kamar(self):
        print(f"Barang di kamar {self.kamar.nomor_kamar}:")

        if len(self.kamar.barang_list) == 0:
            print("- Tidak ada barang")
        else:
            for barang in self.kamar.barang_list:
                print(
                    f"- {barang.nama_barang} "
                    f"(Stok: {barang.stok})"
                )

    @classmethod
    def tampilkan_total_penghuni(cls):
        print(f"Total objek penghuni: {cls.total_penghuni}")

    @staticmethod
    def validasi_nama(nama):
        return nama.strip() != ""

print("=" * 60)
print("SISTEM PENDATAAN BARANG DI KAMAR KOS")
print("=" * 60)

print("\n--- 1. PEMBUATAN OBJEK BARANG ---")

barang1 = Barang("B001", "Laptop", 2)
barang2 = Barang("B002", "Kipas Angin", 1)

print("Objek barang berhasil dibuat.")

print("\n--- 2. PEMBUATAN OBJEK KAMAR ---")

kamar1 = Kamar("101", "Kamar Andi")
kamar2 = Kamar("102", "Kamar Budi")

print("Objek kamar berhasil dibuat.")

print("\n--- 3. PEMBUATAN OBJEK PENGHUNI ---")

penghuni1 = Penghuni("Andi", "231001", kamar1)
penghuni2 = Penghuni("Budi", "231002", kamar2)

print("Objek penghuni berhasil dibuat.")

print("\n--- 4. MENAMBAHKAN BARANG KE KAMAR ---")

kamar1.tambah_barang(barang1)
kamar1.tambah_barang(barang2)

kamar2.tambah_barang(barang2)

print("Barang berhasil ditambahkan ke kamar.")

print("\n--- 5. DATA BARANG ---")

barang1.tampilkan_info()

print()

barang2.tampilkan_info()

print("\n--- 6. DATA KAMAR ---")

kamar1.tampilkan_info()

print()

kamar2.tampilkan_info()

print("\n--- 7. DATA PENGHUNI ---")

penghuni1.tampilkan_info()

print()

penghuni2.tampilkan_info()

print("\n--- 8. PENGUJIAN INSTANCE METHOD ---")

print("Stok Laptop sebelum ditambah:", barang1.stok)

barang1.tambah_stok(3)

print("Stok Laptop setelah ditambah:", barang1.stok)

barang1.kurangi_stok(1)

print("Stok Laptop setelah dikurangi:", barang1.stok)

print("\nBarang yang ada di kamar Andi:")
penghuni1.tampilkan_barang_kamar()

print("\n--- 9. PENGUJIAN CLASS METHOD ---")

Barang.tampilkan_total_barang()
Kamar.tampilkan_total_kamar()
Penghuni.tampilkan_total_penghuni()

print("\nNama sistem sebelum diubah:")
print(Barang.nama_sistem)

Barang.ubah_nama_sistem("Sistem Pendataan Barang Kamar Kos")

print("Nama sistem setelah diubah:")
print(Barang.nama_sistem)

print("\n--- 10. PENGUJIAN STATIC METHOD ---")

print(
    "Validasi nama 'Laptop':",
    Barang.validasi_nama("Laptop")
)

print(
    "Validasi nama kosong:",
    Barang.validasi_nama("")
)

print(
    "Validasi kode 'B001':",
    Barang.validasi_kode("B001")
)

print(
    "Validasi kode kosong:",
    Barang.validasi_kode("")
)

print("\n--- 11. ATRIBUT PUBLIC ---")

print("Nama barang:", barang1.nama_barang)
print("Kode barang:", barang1.kode_barang)
print("\n--- 12. PROPERTY GETTER ---")

print("Stok barang melalui property:", barang1.stok)

print("\n--- 13. ATRIBUT PRIVATE ---")

print("Atribut stok disimpan sebagai atribut private __stok.")
print("Atribut private tidak digunakan secara langsung.")
print("Akses stok dilakukan melalui property 'stok'.")
print("\n--- 14. SETTER DATA VALID ---")

try:
    barang1.stok = 10
    print("Setter berhasil.")
    print("Stok baru:", barang1.stok)

except ValueError as error:
    print("Data ditolak:", error)

print("\n--- 15. SETTER DATA TIDAK VALID ---")

try:
    barang1.stok = -5
    print("Setter berhasil.")

except ValueError as error:
    print("Data ditolak:", error)

print("\n--- 16. SETTER DENGAN TIPE DATA SALAH ---")

try:
    barang1.stok = "banyak"
    print("Setter berhasil.")

except ValueError as error:
    print("Data ditolak:", error)

print("\n" + "=" * 60)
print("PENGUJIAN PROGRAM SELESAI")
print("=" * 60)
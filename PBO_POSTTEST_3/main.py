from abc import ABC, abstractmethod
from copy import copy


class Barang(ABC):
    """Kelas abstrak untuk semua barang yang didata."""
    nama_sistem = "Sistem Pendataan Barang di Kamar Kos"
    total_barang = 0

    def __init__(self, kode_barang, nama_barang, stok):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self._stok = stok
        self.__kode_internal = "INTERNAL-" + kode_barang
        Barang.total_barang += 1

    @property
    def stok(self):
        return self._stok

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            return False
        self._stok += jumlah
        return True

    def kurangi_stok(self, jumlah):
        if jumlah <= 0 or jumlah > self._stok:
            print("Pengurangan stok tidak valid.")
            return False
        self._stok -= jumlah
        return True

    def cek_kode_internal(self):
        return self.__kode_internal

    def tampilkan_ringkas(self):
        """Method konkret yang diwariskan semua subclass."""
        print(f"{self.kode_barang} | {self.nama_barang} | Stok: {self.stok} | {self.kategori()}")

    @abstractmethod
    def tampilkan_info(self):
        """Setiap jenis barang menampilkan informasi khususnya."""
        raise NotImplementedError

    @abstractmethod
    def kategori(self):
        """Mengembalikan nama kategori barang."""
        raise NotImplementedError

    def __str__(self):
        return f"{self.kode_barang} - {self.nama_barang} (stok: {self.stok})"

    def __eq__(self, barang_lain):
        if not isinstance(barang_lain, Barang):
            return NotImplemented
        return self.kode_barang == barang_lain.kode_barang


class BarangElektronik(Barang):
    def __init__(self, kode_barang, nama_barang, stok, daya_watt):
        super().__init__(kode_barang, nama_barang, stok)
        self.daya_watt = daya_watt

    def kategori(self):
        return "Elektronik"

    def tampilkan_info(self):
        print("=== Barang Elektronik ===")
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self.stok}")
        print(f"Daya        : {self.daya_watt} Watt")


class BarangPribadi(Barang):
    def __init__(self, kode_barang, nama_barang, stok, bahan):
        super().__init__(kode_barang, nama_barang, stok)
        self.bahan = bahan

    def kategori(self):
        return "Barang pribadi"

    def tampilkan_info(self):
        print("=== Barang Pribadi ===")
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self.stok}")
        print(f"Bahan       : {self.bahan}")


class CatatanBarang:
    """Objek catatan dibuat dan dikelola oleh Kamar (komposisi)."""
    def __init__(self, id_catatan, keterangan):
        self.id_catatan = id_catatan
        self.keterangan = keterangan

    def __str__(self):
        return f"{self.id_catatan} - {self.keterangan}"


class Kamar:
    total_kamar = 0

    def __init__(self, nomor_kamar, nama_kamar):
        self.nomor_kamar = nomor_kamar
        self.nama_kamar = nama_kamar
        self.barang_list = []
        self.catatan_list = []
        Kamar.total_kamar += 1

    def tambah_barang(self, barang):
        if not isinstance(barang, Barang):
            print("Data bukan objek Barang.")
            return False
        if barang in self.barang_list:
            print("Kode barang tersebut sudah ada di kamar ini.")
            return False
        self.barang_list.append(barang)
        print(f"{barang.nama_barang} berhasil ditambahkan ke kamar {self.nomor_kamar}.")
        return True

    def cari_barang(self, kode_barang):
        for barang in self.barang_list:
            if barang.kode_barang.lower() == kode_barang.lower():
                return barang
        return None

    def tampilkan_barang(self):
        print(f"\n=== Barang di Kamar {self.nomor_kamar} ===")
        if not self.barang_list:
            print("Belum ada barang.")
            return
        for barang in self.barang_list:
            barang.tampilkan_info()
            print()

    def tambah_catatan(self, keterangan):
        id_catatan = f"CAT-{len(self.catatan_list) + 1:03d}"
        catatan = CatatanBarang(id_catatan, keterangan)
        self.catatan_list.append(catatan)
        print("Catatan barang berhasil ditambahkan.")

    def tampilkan_catatan(self):
        print(f"\n=== Catatan Kamar {self.nomor_kamar} ===")
        if not self.catatan_list:
            print("Belum ada catatan.")
            return
        for catatan in self.catatan_list:
            print(catatan)


class Penghuni:
    """Berhubungan dengan Kamar, tetapi bukan pemilik siklus hidupnya."""
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tempati_kamar(self, kamar):
        print(f"{self.nama} (NIM {self.nim}) menempati kamar {kamar.nomor_kamar} ({kamar.nama_kamar}).")


class LaporanTeks:
    def __init__(self, pesan):
        self.pesan = pesan

    def kirim(self):
        print(f"[LAPORAN] {self.pesan}")


class NotifikasiKonsol:
    def __init__(self, pesan):
        self.pesan = pesan

    def kirim(self):
        print(f"[NOTIFIKASI] {self.pesan}")


def proses_pesan(objek):
    """Duck typing: cukup memiliki method kirim()."""
    objek.kirim()


def demonstrasi(kamar, penghuni):
    print("\n--- ASOSIASI ---")
    penghuni.tempati_kamar(kamar)

    print("\n--- POLIMORFISME MELALUI INHERITANCE ---")
    for barang in kamar.barang_list:
        barang.tampilkan_info()
        print()

    print("--- DUCK TYPING ---")
    proses_pesan(LaporanTeks("Pendataan barang kamar selesai."))
    proses_pesan(NotifikasiKonsol("Ada data barang yang diperbarui."))

    print("--- OPERATOR OVERLOADING ---")
    if kamar.barang_list:
        barang = kamar.barang_list[0]
        print("str(barang):", str(barang))
        barang_salinan = copy(barang)
        print("Barang berkode sama dianggap sama:", barang == barang_salinan)


def uji_abstract_class():
    print("\n--- PENGUJIAN ABSTRACT CLASS ---")
    try:
        Barang("X001", "Barang abstrak", 1)
    except TypeError as error:
        print(f"TypeError tertangkap: {error}")


def buat_data_awal():
    laptop = BarangElektronik("B001", "Laptop", 1, 65)
    kipas = BarangElektronik("B002", "Kipas Angin", 2, 45)
    tas = BarangPribadi("B003", "Tas Kuliah", 1, "Kanvas")
    kamar = Kamar("101", "Kamar Meilonie")
    for barang in (laptop, kipas, tas):
        kamar.tambah_barang(barang)
    penghuni = Penghuni("Meilonie", "128")
    kamar.tambah_catatan("Laptop digunakan untuk kuliah.")
    kamar.tambah_catatan("Kipas digunakan saat malam hari.")
    return kamar, penghuni


def jalankan_program():
    """Menjalankan demonstrasi sistem secara otomatis tanpa input pengguna."""
    kamar, penghuni = buat_data_awal()

    print("=" * 58)
    print("SISTEM PENDATAAN BARANG DI KAMAR KOS")
    print("=" * 58)

    print("\n1. MENAMPILKAN DATA BARANG")
    kamar.tampilkan_barang()

    print("\n2. MENCARI BARANG")
    hasil = kamar.cari_barang("B002")
    if hasil:
        print("Barang ditemukan:")
        hasil.tampilkan_info()
    else:
        print("Barang tidak ditemukan.")

    print("\n3. MENAMBAH BARANG")
    botol = BarangPribadi("B004", "Botol Minum", 1, "Stainless steel")
    kamar.tambah_barang(botol)

    print("\n4. MEMPERBARUI STOK")
    if botol.tambah_stok(2):
        print(f"Stok {botol.nama_barang} berhasil ditambah. Stok sekarang: {botol.stok}")

    print("\n5. MENAMPILKAN CATATAN KAMAR")
    kamar.tampilkan_catatan()

    print("\n6. MENAMBAHKAN CATATAN")
    kamar.tambah_catatan("Botol minum dibawa saat kuliah.")
    kamar.tampilkan_catatan()

    print("\n7. MENGHAPUS BARANG")
    barang_hapus = kamar.cari_barang("B004")
    if barang_hapus:
        kamar.barang_list.remove(barang_hapus)
        Barang.total_barang -= 1
        print(f"Barang {barang_hapus.nama_barang} berhasil dihapus dari kamar.")

    print("\n8. DEMONSTRASI KONSEP OOP")
    demonstrasi(kamar, penghuni)
    uji_abstract_class()

    print("\n" + "=" * 58)
    print("Demonstrasi program selesai.")
    print("=" * 58)


if __name__ == "__main__":
    jalankan_program()

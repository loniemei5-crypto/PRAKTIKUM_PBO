class Barang:
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
        if jumlah > 0:
            self._stok += jumlah
            print(f"Stok {self.nama_barang} bertambah {jumlah}.")
        else:
            print("Jumlah harus lebih dari 0.")

    def kurangi_stok(self, jumlah):
        if jumlah > 0 and jumlah <= self._stok:
            self._stok -= jumlah
            print(f"Stok {self.nama_barang} berkurang {jumlah}.")
        else:
            print("Pengurangan stok tidak valid.")

    def tampilkan_info(self):
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self._stok}")

    def cek_kode_internal(self):
        return self.__kode_internal

class BarangElektronik(Barang):

    def __init__(self, kode_barang, nama_barang, stok, daya_watt):
        super().__init__(kode_barang, nama_barang, stok)

        self.daya_watt = daya_watt

    def tampilkan_info(self):
        print("=== Barang Elektronik ===")
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self._stok}")
        print(f"Daya        : {self.daya_watt} Watt")

class BarangPribadi(Barang):

    def __init__(self, kode_barang, nama_barang, stok, bahan):
        super().__init__(kode_barang, nama_barang, stok)

        self.bahan = bahan

    def tampilkan_info(self):
        print("=== Barang Pribadi ===")
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self._stok}")
        print(f"Bahan       : {self.bahan}")

class CatatanBarang:

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
        if isinstance(barang, Barang):
            self.barang_list.append(barang)
            print(
                f"{barang.nama_barang} berhasil ditambahkan "
                f"ke kamar {self.nomor_kamar}."
            )
        else:
            print("Data bukan objek Barang.")

    def tampilkan_barang(self):
        print(f"\n=== Barang di Kamar {self.nomor_kamar} ===")

        if len(self.barang_list) == 0:
            print("Belum ada barang.")
        else:
            for barang in self.barang_list:
                barang.tampilkan_info()
                print()

    def tambah_catatan(self, keterangan):
        id_catatan = f"CAT-{len(self.catatan_list) + 1:03d}"

        # Objek CatatanBarang dibuat langsung di dalam Kamar
        catatan = CatatanBarang(id_catatan, keterangan)

        self.catatan_list.append(catatan)

        print("Catatan barang berhasil ditambahkan.")

    def tampilkan_catatan(self):
        print(f"\n=== Catatan Kamar {self.nomor_kamar} ===")

        if len(self.catatan_list) == 0:
            print("Belum ada catatan.")
        else:
            for catatan in self.catatan_list:
                print(catatan)

class Penghuni:

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tempati_kamar(self, kamar):
        print(
            f"{self.nama} (NIM {self.nim}) "
            f"menempati kamar {kamar.nomor_kamar} "
            f"({kamar.nama_kamar})."
        )

print("=" * 50)
print("SISTEM PENDATAAN BARANG DI KAMAR KOS")
print("=" * 50)

laptop = BarangElektronik(
    "B001",
    "Laptop",
    1,
    65
)

kipas = BarangElektronik(
    "B002",
    "Kipas Angin",
    2,
    45
)

tas = BarangPribadi(
    "B003",
    "Tas Kuliah",
    1,
    "Kanvas"
)

kamar101 = Kamar("101", "Kamar Meilonie")

meilonie = Penghuni("Meilonie", "128")

print("\n--- ASOSIASI ---")

meilonie.tempati_kamar(kamar101)

print("\n--- AGREGASI ---")

kamar101.tambah_barang(laptop)
kamar101.tambah_barang(kipas)
kamar101.tambah_barang(tas)

kamar101.tampilkan_barang()

print("\n--- KOMPOSISI ---")

kamar101.tambah_catatan("Laptop digunakan untuk kuliah.")
kamar101.tambah_catatan("Kipas digunakan saat malam hari.")

kamar101.tampilkan_catatan()

print("\n--- INHERITANCE ---")

laptop.tampilkan_info()
print()

tas.tampilkan_info()

print("\n--- PROTECTED ---")

print(f"Stok laptop: {laptop._stok}")

print("\n--- SUPERCLASS METHOD ---")

laptop.tambah_stok(1)
print(f"Stok laptop setelah ditambah: {laptop.stok}")

print("\n--- PRIVATE ---")

print(f"Kode internal laptop: {laptop.cek_kode_internal()}")

print("\n--- PENGUJIAN INHERITANCE ---")

print(
    "Apakah laptop merupakan Barang?",
    isinstance(laptop, Barang)
)

print(
    "Apakah tas merupakan Barang?",
    isinstance(tas, Barang)
)

print(
    "Apakah BarangElektronik subclass Barang?",
    issubclass(BarangElektronik, Barang)
)

print(
    "Apakah BarangPribadi subclass Barang?",
    issubclass(BarangPribadi, Barang)
)

print("\n--- TOTAL DATA ---")

print(f"Total barang : {Barang.total_barang}")
print(f"Total kamar  : {Kamar.total_kamar}")

print("\nProgram selesai.")
# SISTEM PENDATAAN BARANG DI KAMAR KOS
**Nama:** Meilonie  
**NIM:** 128  
**Mata Kuliah:** Pemrograman Berorientasi Objek  
**Judul Program:** Sistem Pendataan Barang di Kamar Kos

---

## 1. Deskripsi Program

Sistem Pendataan Barang di Kamar Kos merupakan program berbasis Python yang digunakan untuk melakukan pendataan barang yang terdapat di dalam kamar kos.

Program ini dikembangkan dengan menerapkan konsep Pemrograman Berorientasi Objek (OOP), khususnya:

- Class dan Object
- Encapsulation
- Inheritance
- Superclass dan Subclass
- `super().__init__()`
- Method Overriding
- Protected Attribute
- Private Attribute
- Asosiasi
- Agregasi
- Komposisi

Program menggunakan beberapa class utama, yaitu `Barang`, `BarangElektronik`, `BarangPribadi`, `Kamar`, `CatatanBarang`, dan `Penghuni`.

---

## 2. Tujuan Program

Tujuan dari program ini adalah:

1. Mendata barang yang terdapat di dalam kamar kos.
2. Membedakan jenis barang berdasarkan karakteristiknya.
3. Menerapkan konsep inheritance pada class barang.
4. Menerapkan hubungan asosiasi, agregasi, dan komposisi.
5. Menerapkan protected dan private attribute.
6. Menerapkan method overriding.
7. Menunjukkan hubungan antar class dalam sebuah sistem sederhana.

---

## 3. Struktur Class

```text
Barang
├── BarangElektronik
└── BarangPribadi

Kamar
└── CatatanBarang

Penghuni
```

`Barang` merupakan superclass, sedangkan `BarangElektronik` dan `BarangPribadi` merupakan subclass.

---

## 4. Superclass dan Subclass

### 4.1 Superclass Barang

Class `Barang` digunakan sebagai parent class atau superclass.

Atribut yang dimiliki:

- `kode_barang`
- `nama_barang`
- `_stok`
- `__kode_internal`

Method yang dimiliki antara lain:

- `tambah_stok()`
- `kurangi_stok()`
- `tampilkan_info()`
- `cek_kode_internal()`

### 4.2 Subclass BarangElektronik

`BarangElektronik` merupakan subclass dari `Barang`.

```python
class BarangElektronik(Barang):
```

Class ini memiliki atribut khusus:

```python
daya_watt
```

Contoh barang:

- Laptop
- Kipas Angin

Subclass menggunakan konstruktor superclass dengan:

```python
super().__init__(kode_barang, nama_barang, stok)
```

### 4.3 Subclass BarangPribadi

`BarangPribadi` juga merupakan subclass dari `Barang`.

```python
class BarangPribadi(Barang):
```

Class ini memiliki atribut khusus:

```python
bahan
```

Contoh barang:

- Tas Kuliah
- Barang pribadi lainnya

Subclass juga menggunakan:

```python
super().__init__(kode_barang, nama_barang, stok)
```

---

## 5. Penggunaan Inheritance

Inheritance digunakan karena `BarangElektronik` dan `BarangPribadi` merupakan jenis dari `Barang`.

Hubungannya:

```text
BarangElektronik adalah Barang
BarangPribadi adalah Barang
```

Dengan inheritance, kedua subclass dapat menggunakan atribut dan method yang dimiliki oleh superclass.

---

## 6. Penggunaan super()

Pada setiap subclass digunakan:

```python
super().__init__(kode_barang, nama_barang, stok)
```

`super()` digunakan untuk memanggil konstruktor milik superclass `Barang`.

Dengan demikian atribut umum seperti `kode_barang`, `nama_barang`, dan `_stok` tidak perlu ditulis ulang pada subclass.

---

## 7. Method Overriding

Method `tampilkan_info()` terdapat pada superclass `Barang`.

Kemudian method tersebut didefinisikan kembali pada subclass.

Contoh:

```python
def tampilkan_info(self):
    print("=== Barang Elektronik ===")
```

dan:

```python
def tampilkan_info(self):
    print("=== Barang Pribadi ===")
```

Dengan overriding, setiap subclass dapat menampilkan informasi sesuai karakteristik barangnya masing-masing.

---

## 8. Protected Attribute

Program menggunakan atribut protected:

```python
self._stok = stok
```

Atribut `_stok` digunakan sebagai protected karena data stok perlu diakses oleh subclass.

Contohnya pada `BarangElektronik`:

```python
print(f"Stok        : {self._stok}")
```

---

## 9. Private Attribute

Program juga menggunakan private attribute:

```python
self.__kode_internal = "INTERNAL-" + kode_barang
```

Atribut tersebut hanya dapat digunakan secara langsung dari dalam class `Barang`.

Untuk mengaksesnya digunakan method:

```python
def cek_kode_internal(self):
    return self.__kode_internal
```

Private attribute digunakan untuk menunjukkan data yang bersifat internal pada superclass.

---

# 10. Relasi UML

Program menerapkan tiga relasi UML yang diwajibkan, yaitu:

1. Asosiasi
2. Agregasi
3. Komposisi

Selain ketiga relasi tersebut, program juga menerapkan inheritance.

---

## 10.1 Asosiasi

Asosiasi diterapkan antara:

```text
Penghuni → Kamar
```

Penghuni menggunakan objek `Kamar` melalui method:

```python
def tempati_kamar(self, kamar):
```

Contoh penggunaan:

```python
meilonie.tempati_kamar(kamar101)
```

Objek `Kamar` diberikan sebagai parameter kepada method `tempati_kamar()`.

Relasi ini merupakan asosiasi karena `Penghuni` menggunakan `Kamar` tanpa membuat objek `Kamar` di dalam class `Penghuni`.

---

## 10.2 Agregasi

Agregasi diterapkan antara:

```text
Kamar ◇── Barang
```

Barang dibuat di luar class `Kamar`.

Contohnya:

```python
laptop = BarangElektronik("B001", "Laptop", 1, 65)
```

Kemudian barang dimasukkan ke dalam kamar:

```python
kamar101.tambah_barang(laptop)
```

Barang disimpan pada:

```python
self.barang_list = []
```

Karena barang dibuat secara mandiri sebelum dimasukkan ke kamar, hubungan ini merupakan agregasi.

---

## 10.3 Komposisi

Komposisi diterapkan antara:

```text
Kamar ◆── CatatanBarang
```

Objek `CatatanBarang` dibuat langsung di dalam class `Kamar`.

Contohnya:

```python
catatan = CatatanBarang(id_catatan, keterangan)
```

Kemudian dimasukkan ke:

```python
self.catatan_list.append(catatan)
```

Dengan demikian `CatatanBarang` merupakan bagian dari `Kamar` dan dibuat oleh `Kamar`.

---

# 11. Diagram UML Sederhana

```text
                         +----------------------+
                         |       Barang         |
                         +----------------------+
                         | kode_barang          |
                         | nama_barang          |
                         | # _stok              |
                         | - __kode_internal    |
                         +----------------------+
                         | tambah_stok()        |
                         | kurangi_stok()       |
                         | tampilkan_info()     |
                         +----------------------+
                              △          △
                              |          |
                 +------------+          +-------------+
                 |                                     |
    +-------------------------+           +-------------------------+
    |   BarangElektronik      |           |     BarangPribadi       |
    +-------------------------+           +-------------------------+
    | daya_watt               |           | bahan                   |
    +-------------------------+           +-------------------------+
    | tampilkan_info()        |           | tampilkan_info()        |
    +-------------------------+           +-------------------------+


+-------------------+          +-------------------+
|     Penghuni      |          |       Kamar       |
+-------------------+          +-------------------+
| nama              |          | nomor_kamar       |
| nim               |          | nama_kamar        |
+-------------------+          | barang_list       |
| tempati_kamar()   |          | catatan_list      |
+-------------------+          +-------------------+
          |                         /       \
          |                        /         \
       asosiasi               agregasi     komposisi
          |                    ◇ /             \ ◆
          +----------------> Barang       CatatanBarang
```

---

# 12. Contoh Objek

```python
laptop = BarangElektronik(
    "B001",
    "Laptop",
    1,
    65
)
```

```python
kipas = BarangElektronik(
    "B002",
    "Kipas Angin",
    2,
    45
)
```

```python
tas = BarangPribadi(
    "B003",
    "Tas Kuliah",
    1,
    "Kanvas"
)
```

Objek kamar:

```python
kamar101 = Kamar(
    "101",
    "Kamar Meilonie"
)
```

Objek penghuni:

```python
meilonie = Penghuni(
    "Meilonie",
    "128"
)
```

---

# 13. Contoh Proses Program

### Asosiasi

```python
meilonie.tempati_kamar(kamar101)
```

Output:

```text
Meilonie (NIM 128) menempati kamar 101 (Kamar Meilonie).
```

### Agregasi

```python
kamar101.tambah_barang(laptop)
```

Output:

```text
Laptop berhasil ditambahkan ke kamar 101.
```

### Komposisi

```python
kamar101.tambah_catatan(
    "Laptop digunakan untuk kuliah."
)
```

Output:

```text
Catatan barang berhasil ditambahkan.
```

### Inheritance

```python
laptop.tampilkan_info()
```

Output:

```text
=== Barang Elektronik ===
Kode Barang : B001
Nama Barang : Laptop
Stok        : 1
Daya        : 65 Watt
```

---

# 14. Pengujian Inheritance

Program juga melakukan pengujian:

```python
isinstance(laptop, Barang)
```

Hasil:

```text
True
```

Artinya objek `laptop` merupakan objek dari `BarangElektronik` sekaligus merupakan `Barang`.

Pengujian subclass:

```python
issubclass(BarangElektronik, Barang)
```

Hasil:

```text
True
```

Begitu juga:

```python
issubclass(BarangPribadi, Barang)
```

Hasil:

```text
True
```

---

# 15. Kesimpulan

Program Sistem Pendataan Barang di Kamar Kos telah menerapkan konsep Pemrograman Berorientasi Objek sesuai dengan materi yang dipelajari.

Konsep inheritance diterapkan menggunakan `Barang` sebagai superclass dan `BarangElektronik` serta `BarangPribadi` sebagai subclass. Kedua subclass menggunakan `super().__init__()`, mempunyai atribut khusus, serta melakukan method overriding pada method `tampilkan_info()`.

Program juga menerapkan protected attribute `_stok` dan private attribute `__kode_internal`.

Selain inheritance, program menerapkan tiga relasi UML, yaitu asosiasi antara `Penghuni` dan `Kamar`, agregasi antara `Kamar` dan `Barang`, serta komposisi antara `Kamar` dan `CatatanBarang`.

Dengan penerapan tersebut, program dapat menunjukkan hubungan antar objek dan hubungan pewarisan antar class dalam sebuah sistem pendataan barang di kamar kos.

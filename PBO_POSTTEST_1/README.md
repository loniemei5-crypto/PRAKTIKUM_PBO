# Sistem Pendataan Barang di Kamar Kos

## A. Deskripsi Program

Sistem Pendataan Barang di Kamar Kos adalah program sederhana menggunakan bahasa Python dengan pendekatan Object-Oriented Programming (OOP).

Program ini digunakan untuk mendata barang yang terdapat di kamar kos serta menghubungkan data barang dengan kamar dan penghuni.

Program dibuat untuk menerapkan materi:

* Class & Object
* Atribut & Method
* Encapsulation & Property

Program dibuat sederhana agar mudah dipahami dan menunjukkan penerapan konsep dasar OOP.

---

## B. Konsep OOP yang Digunakan

### 1. Class

Program memiliki tiga class utama:

* `Barang`
* `Kamar`
* `Penghuni`

Class digunakan sebagai cetakan untuk membuat objek.

### 2. Object

Object dibuat dari class yang sudah dibuat.

Contoh:

```python
barang1 = Barang("B001", "Laptop", 2)
barang2 = Barang("B002", "Kipas Angin", 1)
```

### 3. Atribut Kelas

Atribut kelas merupakan atribut yang digunakan bersama oleh objek dalam satu class.

Contohnya:

```python
nama_sistem
total_barang
kategori_default
```

Atribut kelas digunakan untuk menyimpan informasi yang bersifat umum.

### 4. Atribut Instance

Atribut instance dibuat menggunakan `self` di dalam `__init__()`.

Contohnya:

```python
self.nama_barang
self.kode_barang
self.__stok
```

Nilainya dapat berbeda untuk setiap objek.

### 5. Public Attribute

Atribut public dapat diakses secara langsung.

Contoh:

```python
self.nama_barang
self.kode_barang
```

Penggunaan:

```python
print(barang1.nama_barang)
```

### 6. Private Attribute

Atribut private menggunakan double underscore.

Contoh:

```python
self.__stok
```

Atribut ini digunakan untuk menyimpan data stok agar aksesnya dapat dikontrol melalui property.

### 7. Instance Method

Instance method menggunakan parameter `self`.

Contohnya:

```python
def tambah_stok(self, jumlah):
```

Method ini digunakan untuk menambah stok barang.

### 8. Class Method

Class method menggunakan decorator `@classmethod` dan parameter `cls`.

Contohnya:

```python
@classmethod
def ubah_nama_sistem(cls, nama_baru):
    cls.nama_sistem = nama_baru
```

Class method digunakan untuk mengubah atribut kelas atau mengakses data yang dimiliki class.

### 9. Static Method

Static method menggunakan decorator `@staticmethod`.

Contohnya:

```python
@staticmethod
def validasi_nama(nama):
    return nama.strip() != ""
```

Static method digunakan sebagai fungsi bantuan untuk validasi data.

### 10. Encapsulation

Encapsulation digunakan dengan menyembunyikan atribut stok menggunakan:

```python
self.__stok
```

Akses terhadap stok dilakukan melalui property.

### 11. Property Getter

Getter digunakan untuk mengambil nilai private attribute.

```python
@property
def stok(self):
    return self.__stok
```

### 12. Property Setter

Setter digunakan untuk mengubah nilai stok sekaligus melakukan validasi.

```python
@stok.setter
def stok(self, nilai):
    if not isinstance(nilai, int):
        raise ValueError("Stok harus berupa angka bulat.")

    if nilai < 0:
        raise ValueError("Stok tidak boleh negatif.")

    self.__stok = nilai
```

### 13. Validasi Data

Program melakukan validasi terhadap data stok.

Stok:

* harus berupa angka bulat
* tidak boleh negatif

Jika data tidak valid, program menggunakan `raise ValueError`.

---

## C. Struktur Class

| Class      | Fungsi                                      | Atribut Utama                              | Method                                                                                         |
| ---------- | ------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `Barang`   | Menyimpan data barang                       | `kode_barang`, `nama_barang`, `__stok`     | `tampilkan_info()`, `tambah_stok()`, `kurangi_stok()`, `ubah_nama_sistem()`, `validasi_nama()` |
| `Kamar`    | Menyimpan data kamar dan barang di dalamnya | `nomor_kamar`, `nama_kamar`, `barang_list` | `tampilkan_info()`, `tambah_barang()`, `tampilkan_total_kamar()`                               |
| `Penghuni` | Menyimpan data penghuni dan kamar           | `nama`, `nim`, `kamar`                     | `tampilkan_info()`, `tampilkan_barang_kamar()`, `tampilkan_total_penghuni()`                   |

---

## D. Hubungan Antar-Class

Hubungan antar-class dibuat sederhana.

```text
Penghuni
   |
   | menempati
   v
 Kamar
   |
   | memiliki
   v
 Barang
```

Contohnya:

```text
Andi → Kamar 101 → Laptop, Kipas Angin
Budi → Kamar 102 → Kipas Angin
```

Objek `Penghuni` menyimpan objek `Kamar`, sedangkan objek `Kamar` memiliki daftar objek `Barang`.

---

## E. Struktur File

```text
Sistem-Pendataan-Barang-Kos/
│
├── main.py
└── README.md
```

Keterangan:

* `main.py` berisi seluruh kode program.
* `README.md` berisi dokumentasi program.

---

## F. Panduan Menjalankan Program

### 1. Pastikan Python sudah terinstal

Cek menggunakan terminal:

```bash
python --version
```

### 2. Masuk ke folder project

Contoh:

```bash
cd Sistem-Pendataan-Barang-Kos
```

### 3. Jalankan program

```bash
python main.py
```

Program akan menampilkan hasil pengujian pada terminal.

---

## G. Panduan Pengujian

Program melakukan beberapa pengujian:

### 1. Membuat Object

Dibuat minimal dua objek untuk setiap class.

Contoh:

```python
barang1 = Barang("B001", "Laptop", 2)
barang2 = Barang("B002", "Kipas Angin", 1)
```

### 2. Menampilkan Data

Data barang, kamar, dan penghuni ditampilkan menggunakan instance method.

### 3. Menguji Instance Method

Contoh:

```python
barang1.tambah_stok(3)
```

### 4. Menguji Class Method

Contoh:

```python
Barang.tampilkan_total_barang()
```

### 5. Menguji Static Method

Contoh:

```python
Barang.validasi_nama("Laptop")
```

### 6. Menguji Getter

Contoh:

```python
print(barang1.stok)
```

### 7. Menguji Setter dengan Data Valid

Contoh:

```python
barang1.stok = 10
```

Data diterima karena nilai stok berupa angka dan tidak negatif.

### 8. Menguji Setter dengan Data Tidak Valid

Contoh:

```python
barang1.stok = -5
```

Data ditolak karena stok tidak boleh negatif.

Pengujian tipe data juga dilakukan:

```python
barang1.stok = "banyak"
```

Data ditolak karena stok harus berupa angka bulat.

---

## H. Contoh Output

```text
============================================================
SISTEM PENDATAAN BARANG DI KAMAR KOS
============================================================

--- 1. PEMBUATAN OBJEK BARANG ---
Objek barang berhasil dibuat.

--- 2. PEMBUATAN OBJEK KAMAR ---
Objek kamar berhasil dibuat.

--- 3. PEMBUATAN OBJEK PENGHUNI ---
Objek penghuni berhasil dibuat.

--- 4. MENAMBAHKAN BARANG KE KAMAR ---
Barang berhasil ditambahkan ke kamar.

--- 5. DATA BARANG ---
Kode Barang : B001
Nama Barang : Laptop
Stok        : 2

--- 8. PENGUJIAN INSTANCE METHOD ---
Stok Laptop sebelum ditambah: 2
Stok Laptop setelah ditambah: 5
Stok Laptop setelah dikurangi: 4

--- 9. PENGUJIAN CLASS METHOD ---
Total objek barang: 2
Total objek kamar: 2
Total objek penghuni: 2

--- 10. PENGUJIAN STATIC METHOD ---
Validasi nama 'Laptop': True
Validasi nama kosong: False

--- 12. PROPERTY GETTER ---
Stok barang melalui property: 4

--- 14. SETTER DATA VALID ---
Setter berhasil.
Stok baru: 10

--- 15. SETTER DATA TIDAK VALID ---
Data ditolak: Stok tidak boleh negatif.

--- 16. SETTER DENGAN TIPE DATA SALAH ---
Data ditolak: Stok harus berupa angka bulat.

============================================================
PENGUJIAN PROGRAM SELESAI
============================================================
```
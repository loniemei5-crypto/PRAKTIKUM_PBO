# SISTEM PENDATAAN BARANG DI KAMAR KOS
**Nama:** Meilonie  
**NIM:** 128  
**Mata Kuliah:** Pemrograman Berorientasi Objek  
**Judul Program:** Sistem Pendataan Barang di Kamar Kos
# Sistem Pendataan Barang di Kamar Kos

## 1. Judul dan Deskripsi Program

**Sistem Pendataan Barang di Kamar Kos** merupakan program berbasis Python yang menerapkan konsep Object-Oriented Programming (OOP) untuk melakukan pendataan dan pengelolaan barang di kamar kos. Program ini dirancang untuk menampilkan informasi barang, mencari barang berdasarkan kode, menambahkan barang, memperbarui stok, mengelola catatan kamar, serta menghapus barang dari daftar.

Program menggunakan beberapa kelas, yaitu `Barang`, `BarangElektronik`, `BarangPribadi`, `Kamar`, `CatatanBarang`, `Penghuni`, `LaporanTeks`, dan `NotifikasiKonsol`. Program berjalan secara otomatis menggunakan data awal yang telah ditentukan di dalam kode tanpa menggunakan fungsi `input()`.

Selain pengelolaan data barang, program ini menerapkan konsep abstraksi, inheritance, polimorfisme, duck typing, dan operator overloading.

## 2. Class Diagram

Class diagram menggambarkan struktur kelas, atribut, method, serta hubungan antarkelas dalam Sistem Pendataan Barang di Kamar Kos.

Masukkan gambar class diagram pada bagian ini dengan nama file `class_diagram.png`.

![Class Diagram Sistem Pendataan Barang di Kamar Kos](class_diagram.png)

### 2.1 Penjelasan Relasi Antarkelas

**a. Asosiasi (Association)**

Asosiasi merupakan hubungan antara dua kelas yang saling berinteraksi. Pada program ini, kelas `Penghuni` berhubungan dengan kelas `Kamar` melalui method `tempati_kamar(kamar)`. Method tersebut menampilkan informasi nama penghuni, NIM, nomor kamar, dan nama kamar yang ditempati.

Objek `Penghuni` dan `Kamar` dibuat secara terpisah sehingga keduanya tidak bergantung pada satu sama lain untuk keberadaan objeknya.

**b. Agregasi (Aggregation)**

Agregasi diterapkan pada hubungan antara kelas `Kamar` dan kelas `Barang`. Kelas `Kamar` menyimpan kumpulan objek barang melalui atribut `barang_list`.

Method `tambah_barang(barang)` digunakan untuk menambahkan objek barang ke dalam daftar kamar. Barang merupakan objek tersendiri sehingga dapat tetap ada meskipun sudah dikeluarkan dari daftar barang kamar.

**c. Komposisi (Composition)**

Komposisi diterapkan pada hubungan antara kelas `Kamar` dan kelas `CatatanBarang`. Kelas `Kamar` menyimpan kumpulan catatan melalui atribut `catatan_list`.

Method `tambah_catatan(keterangan)` membuat objek `CatatanBarang`, kemudian menyimpannya ke dalam daftar catatan kamar. Dalam rancangan program ini, catatan diperlakukan sebagai bagian dari data kamar.

**d. Inheritance (Pewarisan)**

Pewarisan diterapkan melalui kelas abstrak `Barang` sebagai kelas induk. Kelas `BarangElektronik` dan `BarangPribadi` merupakan kelas turunan yang mewarisi atribut dan method dari kelas `Barang`.

Kedua kelas turunan menggunakan `super().__init__()` untuk memanggil konstruktor kelas induk serta mengimplementasikan method abstrak yang diwajibkan.

**e. Duck Typing**

Duck typing diterapkan pada kelas `LaporanTeks` dan `NotifikasiKonsol`. Kedua kelas tidak saling mewarisi, tetapi memiliki method dengan nama yang sama, yaitu `kirim()`.

Fungsi `proses_pesan(objek)` dapat memproses objek dari kedua kelas tersebut karena keduanya menyediakan method `kirim()`.

## 3. Penerapan Abstraksi dan Polimorfisme

### 3.1 Abstraksi (Abstraction)

Abstraksi diterapkan pada kelas `Barang` dengan menggunakan modul `abc`, yaitu melalui pewarisan `ABC` dan dekorator `@abstractmethod`.

Kelas `Barang` memiliki dua method abstrak:

1. `tampilkan_info()`
2. `kategori()`

Method tersebut harus diimplementasikan oleh kelas turunan, yaitu `BarangElektronik` dan `BarangPribadi`.

Kelas `Barang` tidak dapat diinstansiasi secara langsung karena masih memiliki method abstrak yang belum diimplementasikan. Pengujian dilakukan melalui fungsi `uji_abstract_class()` dengan mencoba membuat objek menggunakan perintah:

`Barang("X001", "Barang abstrak", 1)`

Percobaan tersebut menghasilkan `TypeError`, kemudian kesalahan ditangkap menggunakan `try-except` dan ditampilkan sebagai bukti bahwa kelas abstrak tidak dapat dibuat menjadi objek secara langsung.

### 3.2 Polimorfisme (Polymorphism)

Polimorfisme diterapkan melalui method `tampilkan_info()` dan `kategori()` pada kelas `BarangElektronik` dan `BarangPribadi`.

Kedua kelas memiliki method dengan nama yang sama, tetapi implementasinya berbeda sesuai dengan jenis barang.

- Kelas `BarangElektronik` menampilkan kode barang, nama barang, stok, dan daya listrik dalam satuan watt.
- Kelas `BarangPribadi` menampilkan kode barang, nama barang, stok, dan bahan barang.

Polimorfisme ditunjukkan dalam fungsi `demonstrasi(kamar, penghuni)`, ketika program melakukan perulangan terhadap `kamar.barang_list` dan memanggil method `tampilkan_info()` pada setiap objek barang. Dengan demikian, setiap objek menampilkan informasi sesuai dengan kelasnya.

### 3.3 Duck Typing

Duck typing ditunjukkan melalui fungsi `proses_pesan(objek)` yang menjalankan method `objek.kirim()`.

Fungsi tersebut dapat menerima objek `LaporanTeks` maupun `NotifikasiKonsol`. Meskipun kedua kelas tidak memiliki hubungan pewarisan, keduanya dapat diproses karena menyediakan method `kirim()`.

### 3.4 Operator Overloading

Operator overloading diterapkan melalui dua special method pada kelas `Barang`.

1. `__str__()` digunakan untuk menentukan bentuk teks ketika objek barang ditampilkan menggunakan `str(barang)`.
2. `__eq__()` digunakan untuk membandingkan dua objek barang berdasarkan kesamaan nilai `kode_barang` menggunakan operator `==`.

Penerapan tersebut ditunjukkan pada fungsi `demonstrasi()` dengan membuat salinan objek menggunakan `copy(barang)`, kemudian membandingkan objek asli dan salinannya.

## 4. Fitur Program

Program Sistem Pendataan Barang di Kamar Kos memiliki beberapa fitur yang dijalankan secara otomatis, yaitu:

1. Menampilkan data barang yang terdapat di kamar.
2. Mencari barang berdasarkan kode barang.
3. Menambahkan barang baru ke dalam daftar kamar.
4. Memperbarui jumlah stok barang.
5. Menampilkan catatan kamar.
6. Menambahkan catatan baru pada kamar.
7. Menghapus barang dari daftar kamar.
8. Menampilkan informasi penghuni dan kamar yang ditempati.
9. Mendemonstrasikan inheritance dan polimorfisme.
10. Mendemonstrasikan duck typing dan operator overloading.
11. Menguji abstraksi dengan membuktikan bahwa kelas `Barang` tidak dapat diinstansiasi secara langsung.

## 5. Screenshot Output Program

Screenshot digunakan sebagai bukti bahwa program berhasil dijalankan dan konsep OOP telah diterapkan sesuai rancangan.

### 5.1 Screenshot Output Utama

screenshot hasil menjalankan program yang memperlihatkan judul program, data barang, proses pencarian barang, penambahan barang, pembaruan stok, dan pengelolaan catatan kamar.

## 6. Kesimpulan

Sistem Pendataan Barang di Kamar Kos merupakan program Python yang menerapkan konsep Object-Oriented Programming untuk mengelola data barang secara terstruktur. Abstraksi diterapkan melalui kelas `Barang`, sedangkan inheritance diterapkan melalui kelas `BarangElektronik` dan `BarangPribadi`.

Polimorfisme ditunjukkan melalui implementasi method `tampilkan_info()` dan `kategori()` yang memiliki perilaku berbeda sesuai jenis barang. Duck typing diterapkan pada kelas `LaporanTeks` dan `NotifikasiKonsol` melalui method `kirim()`. Selain itu, program menerapkan operator overloading melalui method `__str__()` dan `__eq__()`.

Melalui penerapan konsep tersebut, program menunjukkan bagaimana kelas dan objek dapat digunakan untuk membangun sistem pendataan barang yang terstruktur, mudah dikembangkan, dan sesuai dengan prinsip dasar OOP.
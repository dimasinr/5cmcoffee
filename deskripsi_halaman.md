# Dokumentasi Halaman Web - Sistem Rekomendasi Kopi

Dokumen ini mendeskripsikan seluruh halaman web yang tersedia dalam proyek **Sistem Rekomendasi Kopi (5CM Coffee And Eatery)** berdasarkan berkas-berkas *template* HTML yang berada di direktori `recommendation/templates/`.

---

## 1. Struktur Layout Dasar (Base Templates)

Sistem menggunakan mekanisme pewarisan (*template inheritance*) Django untuk menjaga konsistensi tampilan. Terdapat dua layout dasar utama:

### A. Layout Utama (`base.html`)
* **Lokasi Berkas:** `recommendation/templates/base.html`
* **Deskripsi:** Menjadi kerangka dasar untuk seluruh halaman pengguna umum dan kerangka terluar dari halaman admin.
* **Komponen & Fitur:**
  * **Header/Navbar:** Menampilkan nama kafe (**5CM Coffee And Eatery**) beserta logo berupa ikon cangkir kopi berapi. Menyediakan tombol **Logout** apabila pengguna telah masuk.
  * **Pesan Flash (Messages):** Area notifikasi dinamis untuk menampilkan pesan sukses (*success*) berwarna hijau atau pesan kesalahan (*error*) berwarna merah.
  * **Footer:** Informasi hak cipta statis di bagian bawah halaman.
  * **Desain & Gaya:** Menggunakan TailwindCSS, Google Fonts (Playfair Display & Inter), efek tekstur grain halus, efek kaca (*glassmorphism*), serta animasi *fade-in* transisi.

### B. Layout Panel Admin (`base_admin.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/base_admin.html`
* **Deskripsi:** Mewarisi `base.html` dan menambahkan tata letak panel kontrol khusus untuk pengguna staf/admin.
* **Komponen & Fitur:**
  * **Sidebar Navigasi:** Memiliki dua menu navigasi utama:
    1. **Kelola Data Menu** (Mengarah ke `admin_menu`)
    2. **Kelola Data Pengguna** (Mengarah ke `admin_users`)
  * **Konten Dinamis:** Area utama di sebelah kanan sidebar (`admin_content`) untuk menampilkan tabel data atau formulir administrasi.

---

## 2. Halaman Autentikasi & Akun Pengguna

Halaman-halaman yang digunakan oleh pengunjung untuk mendaftar, masuk, dan keluar dari aplikasi.

### A. Halaman Pendaftaran (`register.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/register.html`
* **Deskripsi:** Halaman bagi pengunjung baru untuk mendaftarkan akun pelanggan.
* **Fitur Utama:**
  * Formulir pendaftaran pengguna (Nama, Email, Password).
  * Validasi input.
  * Tombol tautan menuju halaman Login jika pengguna sudah memiliki akun.

### B. Halaman Masuk (`login.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/login.html`
* **Deskripsi:** Halaman awal bagi semua pengguna (pelanggan maupun admin) untuk mengakses sistem rekomendasi atau panel kontrol.
* **Fitur Utama:**
  * Input kredensial (Email/Username dan Password).
  * Pengalihan otomatis (*redirect*) berdasarkan hak akses: jika admin masuk akan diarahkan ke panel admin, sedangkan pelanggan diarahkan ke formulir preferensi.
  * Tombol tautan menuju halaman Register jika belum memiliki akun.

### C. Halaman Keluar (`logout.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/logout.html`
* **Deskripsi:** Halaman konfirmasi sederhana saat pengguna menekan tombol *Logout*.
* **Fitur Utama:**
  * Pesan konfirmasi: "Apakah Anda yakin ingin keluar?"
  * Tombol konfirmasi tindakan keluar (menggunakan metode POST demi keamanan) dan tombol pembatalan.

---

## 3. Halaman Fitur Utama (Sistem Rekomendasi)

Halaman-halaman inti tempat pelanggan melakukan proses pencarian rekomendasi kopi yang sesuai dengan seleranya.

### A. Halaman Formulir Preferensi (`recommendation_form.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/recommendation_form.html`
* **Deskripsi:** Tempat pengguna memasukkan preferensi rasa kopi yang diinginkan.
* **Fitur Utama & Parameter Input:**
  * **Karakteristik Rasa (Sliders & Radio):**
    * *Kemanisan* (Slider/Range level 1-5 dengan visualisasi angka waktu nyata)
    * *Kepahitan* (Slider/Range level 1-5 dengan visualisasi angka waktu nyata)
    * *Keasaman* (Slider/Range level 1-5 dengan visualisasi angka waktu nyata)
    * *Body* (Slider/Range level 1-5 dengan visualisasi angka waktu nyata)
    * *Aroma* (Pilihan radio button: Ringan / Sedang / Kuat)
  * **Detail Tambahan (Toggle & Radio):**
    * *Susu* (Toggle switch: Dengan Susu / Tanpa Susu)
    * *Suhu* (Toggle switch: Disajikan Panas / Dingin)
    * *Jenis Biji Kopi* (Pilihan radio button: Arabica / Robusta / Blend)
    * *Level Kafein* (Pilihan radio button: Rendah / Sedang / Tinggi)
  * **Tombol Aksi:** "Simpan Preferensi" untuk memproses data menggunakan algoritma KNN.

### B. Halaman Hasil Rekomendasi (`recommendation_result.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/recommendation_result.html`
* **Deskripsi:** Menampilkan daftar 3 menu kopi terbaik hasil analisis algoritma KNN.
* **Fitur Utama:**
  * Grid card berisi 3 menu kopi yang direkomendasikan secara berurutan.
  * **Badge Kemiripan (Similarity):** Menampilkan persentase kemiripan (misal: `95.4%`) di setiap kartu menu.
  * Deskripsi singkat dan gambar menu kopi.
  * Tombol **Cari Lagi** untuk kembali ke halaman preferensi.

### C. Halaman Detail Kopi (`coffee_detail.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/coffee_detail.html`
* **Deskripsi:** Menampilkan informasi lengkap mengenai satu menu kopi tertentu setelah pengguna mengklik salah satu hasil rekomendasi.
* **Fitur Utama:**
  * Gambar menu ukuran besar.
  * Nama menu dan deskripsi lengkap.
  * Bar karakteristik rasa (Manis, Pahit, Asam, Body) dalam format skala 1-5.
  * Tag detail kopi seperti jenis biji, suhu sajian, level kafein, dan status susu.
  * Tautan navigasi "Kembali" ke halaman sebelumnya.

---

## 4. Halaman Administrasi (Admin Panel)

Halaman-halaman yang hanya dapat diakses oleh admin/staf untuk mengelola basis data menu dan pengguna.

### A. Halaman Kelola Data Menu (`admin_menu.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/admin_menu.html`
* **Deskripsi:** Halaman utama manajemen menu kopi yang menampilkan seluruh daftar kopi yang ada di database.
* **Fitur Utama:**
  * Tombol **Tambah Menu** untuk membuka form menu baru.
  * Tabel daftar menu dengan kolom nomor dan nama menu.
  * Tombol aksi di setiap baris tabel: **Detail** (untuk edit) dan **Hapus** (dilengkapi dengan dialog konfirmasi JS).

### B. Halaman Formulir Menu (`admin_menu_form.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/admin_menu_form.html`
* **Deskripsi:** Formulir yang digunakan untuk menambah menu baru maupun menyunting menu kopi yang sudah ada.
* **Fitur Utama:**
  * Mendukung input data teks, pilihan numerik rasa, dan unggah berkas gambar kopi.
  * Deteksi dinamis judul halaman ("Tambah Menu" atau "Edit Menu").

### C. Halaman Kelola Data Pengguna (`admin_users.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/admin_users.html`
* **Deskripsi:** Menampilkan daftar semua pengguna terdaftar dalam sistem.
* **Fitur Utama:**
  * Tombol **Tambah Pengguna**.
  * Tabel data pengguna dengan kolom nama dan email.
  * Proteksi khusus: Akun admin yang sedang aktif diberi label khusus "**Anda**" dan tombol hapusnya dinonaktifkan untuk mencegah terhapusnya akun sendiri secara tidak sengaja.
  * Tombol aksi **Detail** (untuk edit) dan **Hapus** (dengan dialog konfirmasi).

### D. Halaman Formulir Pengguna (`admin_user_form.html`)
* **Lokasi Berkas:** `recommendation/templates/recommendation/admin_user_form.html`
* **Deskripsi:** Formulir untuk menambah pengguna baru secara manual oleh admin atau menyunting informasi pengguna yang sudah terdaftar.
* **Fitur Utama:**
  * Menggunakan skema form Django.
  * Tombol submit dinamis sesuai aksi penambahan atau pengubahan data pengguna.

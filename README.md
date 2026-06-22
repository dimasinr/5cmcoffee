# Coffee Recommendation System

Sistem rekomendasi signature drink kopi berbasis website menggunakan Django dan Tailwind CSS, menggunakan algoritma K-Nearest Neighbor (KNN) untuk mencocokkan preferensi pelanggan dengan menu yang tersedia.

## Persyaratan
- Python 3.10+
- Virtual Environment (disarankan)

## 1. Langkah Setup

1. **Clone repository ini / navigasi ke folder project:**
   ```bash
   cd C:\Users\Impacto\Documents\Skripsi\coffee_recommendation
   ```

2. **Aktifkan Virtual Environment:**
   *(Sesuai path yang diberikan: `C:\Users\Impacto\Documents\Skripsi\venv\Scripts`)*
   ```bash
   C:\Users\Impacto\Documents\Skripsi\venv\Scripts\activate
   ```

3. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

## 2. Media & Static Setup
Folder `media` (untuk upload gambar kopi) dan `static` (untuk aset tambahan jika ada) akan dibuat otomatis atau dilayani oleh Django berkat konfigurasi `MEDIA_URL` dan `STATIC_URL` di `settings.py`.
- URL Media: `/media/`
- Konfigurasi ini sudah ada di `urls.py` project.

## 3. Tailwind Setup
Proyek ini menggunakan **Tailwind CSS via CDN** untuk kemudahan deployment dan instalasi tanpa perlu Node.js. 
Script CDN sudah terpasang di `recommendation/templates/base.html`:
```html
<script src="https://cdn.tailwindcss.com"></script>
```
Semua kelas tailwind dapat langsung digunakan di template.

## 4. Migrate Instructions
Untuk menyiapkan database SQLite bawaan dan tabel-tabelnya:
```bash
python manage.py makemigrations
python manage.py migrate
```
*(Catatan: Langkah ini sudah dijalankan)*

## 5. Menyiapkan Data Awal (Seeding)
Agar sistem rekomendasi bisa berjalan, diperlukan data menu kopi di database. Jalankan command berikut:
```bash
python manage.py seed_coffee_data
```
*(Catatan: Langkah ini sudah dijalankan. 15 menu kopi sudah terisi).*

## 6. Membuat Superuser (Untuk Akses Admin)
Untuk mengelola menu kopi melalui panel admin:
```bash
python manage.py createsuperuser
```
Isi username, email, dan password.

## 7. Menjalankan Aplikasi
Jalankan server pengembangan Django:
```bash
python manage.py runserver
```
Buka browser dan akses:
- **Aplikasi utama:** `http://127.0.0.1:8000/`
- **Panel Admin:** `http://127.0.0.1:8000/admin/`

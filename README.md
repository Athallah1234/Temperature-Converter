# Konverter Suhu dengan Python dan Tkinter

Aplikasi **Konverter Suhu** ini dikembangkan menggunakan **Python** dan **Tkinter** untuk mengonversi suhu antara berbagai satuan, seperti Celsius, Fahrenheit, Kelvin, dan Réaumur. Aplikasi ini memiliki antarmuka yang mudah digunakan dan dilengkapi dengan fitur tambahan seperti riwayat konversi, pemilihan presisi desimal, dan tombol untuk menukar unit suhu.

## Fitur

- Konversi suhu antara Celsius, Fahrenheit, Kelvin, dan Réaumur.
- Pemilihan presisi desimal hasil konversi.
- Riwayat konversi yang menampilkan waktu dan detail setiap konversi.
- Fitur salin otomatis untuk menyalin hasil konversi ke clipboard.
- Tombol untuk menukar unit input dan output dengan mudah.
- Tampilan responsif yang mendukung perubahan ukuran jendela.

## Cara Menggunakan

1. **Masukkan suhu** yang ingin dikonversi di kolom input.
2. Pilih **satuan suhu** input dari menu drop-down.
3. Pilih **satuan suhu** yang ingin dikonversikan.
4. Tentukan **presisi desimal** jika diperlukan.
5. Klik tombol **Convert** untuk melakukan konversi.
6. Hasil konversi akan otomatis disalin ke clipboard dan muncul di riwayat konversi.
7. Gunakan tombol **Swap Units** untuk menukar satuan input dan output.
8. Riwayat konversi akan ditampilkan di panel sebelah kanan.

## Persyaratan Sistem

- Python 3.x
- Modul Tkinter (sudah termasuk dalam distribusi standar Python)
- Modul `ttkthemes` untuk tema UI yang lebih modern.

## Instalasi

1. Clone repository ini atau unduh file kode sumber.
2. Pastikan Anda telah menginstal `ttkthemes` dengan menjalankan perintah berikut:

    ```bash
    pip install ttkthemes
    ```

3. Jalankan file Python:

    ```bash
    python konverter_suhu.py
    ```

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk mengembangkan aplikasi.
- **Tkinter**: Modul GUI standar Python.
- **ttkthemes**: Mengubah tampilan Tkinter menjadi lebih modern dan estetis.

## Kontribusi

Kontribusi sangat diterima! Jika Anda menemukan masalah, punya saran, atau ingin menambahkan fitur baru, silakan ikuti langkah-langkah berikut:
- Fork repository ini.
- Buat branch baru untuk fitur atau perbaikan Anda (``git checkout -b fitur-anda``)
- Commit perubahan Anda (``git commit -am 'Menambahkan fitur baru'``)
- Push ke branch (``git push origin fitur-anda``)
- Buka pull request di GitHub.
Jika Anda menemukan bug atau ingin melaporkan masalah, silakan buka issue di halaman Issues.

## Lisensi

Aplikasi ini dilisensikan di bawah lisensi MIT. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang kode ini, selama tetap menyertakan lisensi ini. Silakan baca [LICENSE](LICENSE) untuk informasi lebih lanjut.

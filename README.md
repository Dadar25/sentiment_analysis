# Sentiment Analysis

## Deskripsi Proyek
Repositori ini berisi program untuk melakukan analisis sentimen pada data ulasan aplikasi di Google Play Store. Proyek ini menggunakan teknik deep learning, khususnya model **Bidirectional LSTM**, untuk mengklasifikasikan sentimen menjadi tiga kategori: **positif**, **netral**, dan **negatif**.

Program ini juga mencakup teknik pra-pemrosesan data, seperti tokenisasi, padding, dan oversampling untuk mengatasi ketidakseimbangan kelas dalam dataset.

## Fitur Utama
- **Pra-pemrosesan Data**:
  - Membersihkan data ulasan dengan menghapus kolom yang tidak relevan.
  - Mengonversi skor ulasan menjadi label sentimen: **positif**, **netral**, dan **negatif**.
  - Tokenisasi dan padding untuk mempersiapkan data untuk deep learning.

- **Pembelajaran Mesin**:
  - Model **Bidirectional LSTM** digunakan untuk mempelajari pola sentimen dalam data teks.
  - Callback khusus untuk menghentikan pelatihan jika akurasi validasi mencapai ambang tertentu.

- **Evaluasi Model**:
  - Menghitung akurasi model.
  - Menampilkan **classification report** dan matriks kebingungan untuk memvisualisasikan performa model.

## Hasil
1. Model mencapai akurasi 85% pada data validasi.
2. Matriks kebingungan menunjukkan distribusi prediksi untuk setiap kategori sentimen.


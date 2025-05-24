# 🎨 Ekstraksi Warna Dominan dari Gambar

Aplikasi web interaktif untuk mengekstrak warna-warna dominan dari gambar menggunakan algoritma K-Means clustering. Dibangun dengan Streamlit dan Python.

## 📋 Deskripsi

Aplikasi ini memungkinkan pengguna untuk mengunggah gambar dan secara otomatis mengekstrak maksimal 5 warna dominan dari gambar tersebut. Aplikasi menggunakan algoritma K-Means clustering untuk mengelompokkan warna-warna yang serupa dan menampilkan hasilnya dalam bentuk palette warna yang interaktif.

## ✨ Fitur

- **Upload Gambar**: Mendukung format JPG, JPEG, dan PNG
- **Ekstraksi Otomatis**: Tidak perlu menekan tombol, warna diekstrak otomatis setelah upload
- **Palette Interaktif**: Hex code dapat diklik dan disalin langsung dari palette
- **Visualisasi K-Means**: Menampilkan visualisasi proses clustering menggunakan PCA
- **Responsive Design**: Interface yang bersih dan user-friendly
- **Adaptasi Warna**: Jumlah warna yang diekstrak disesuaikan dengan warna unik dalam gambar

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+**
- **Streamlit** - Framework web untuk aplikasi data science
- **OpenCV** - Computer vision library untuk pemrosesan gambar
- **scikit-learn** - Machine learning library untuk K-Means dan PCA
- **NumPy** - Numerical computing
- **Matplotlib** - Plotting dan visualisasi

## 📦 Instalasi

1. **Clone repository ini:**
   ```bash
   git clone [repository-url]
   cd ekstraksi-warna-dominan
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit opencv-python scikit-learn numpy matplotlib
   ```

   Atau menggunakan requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi:**
   ```bash
   streamlit run app.py
   ```

4. **Buka browser** dan akses `http://localhost:8501`

## 📁 Struktur File

```
├── app.py                 # File utama aplikasi Streamlit
└── README.md             # Dokumentasi
```

## 🚀 Cara Penggunaan

1. **Upload Gambar**: Klik tombol "Browse files" dan pilih gambar yang ingin dianalisis
2. **Lihat Hasil**: Aplikasi akan otomatis memproses dan menampilkan:
   - Gambar asli
   - Informasi jumlah warna unik
   - Palette warna dominan dengan hex codes
   - Visualisasi K-Means clustering (opsional)
3. **Copy Hex Code**: Klik pada hex code di palette untuk menyalin

## 🔬 Cara Kerja Algoritma

1. **Preprocessing**: Gambar dikonversi dari format BGR ke RGB
2. **Pixel Extraction**: Setiap pixel diambil nilai RGB-nya
3. **K-Means Clustering**: Algoritma mengelompokkan warna yang mirip
4. **Centroid Calculation**: Pusat cluster menjadi warna dominan
5. **Visualization**: PCA mereduksi dimensi RGB (3D) ke 2D untuk visualisasi

## 🎯 Contoh Output

### Input:
- Gambar dengan berbagai warna

### Output:
- Maksimal 5 warna dominan dalam format hex code
- Palette warna interaktif
- Visualisasi clustering (2 plot):
  - Plot dengan warna asli
  - Plot dengan warna cluster

## ⚙️ Konfigurasi

Anda dapat menyesuaikan beberapa parameter dalam kode:

```python
# Jumlah maksimal warna yang diekstrak
max_k = 5

# Jumlah sampel untuk visualisasi (untuk performa)
n_samples = 5000

# Random state untuk konsistensi hasil
random_state = 42
```

## 🔧 Requirements

```txt
streamlit>=1.28.0
opencv-python>=4.8.0
scikit-learn>=1.3.0
numpy>=1.24.0
matplotlib>=3.7.0
```

## 🐛 Troubleshooting

### Error saat install OpenCV:
```bash
pip install opencv-python-headless
```

### Error "No module named cv2":
```bash
pip uninstall opencv-python
pip install opencv-python
```

### Aplikasi tidak bisa diakses:
- Pastikan port 8501 tidak digunakan aplikasi lain
- Coba jalankan dengan port berbeda:
  ```bash
  streamlit run app.py --server.port 8502
  ```

## 📈 Pengembangan Lebih Lanjut

Beberapa ide untuk pengembangan:

- [ ] Export palette ke berbagai format (CSS, SCSS, JSON)
- [ ] Support untuk lebih banyak format gambar
- [ ] Algoritma clustering alternatif (DBSCAN, Hierarchical)
- [ ] Batch processing untuk multiple images
- [ ] API endpoint untuk integrasi eksternal
- [ ] Dark mode toggle
- [ ] Histogram warna

## 👨‍💻 Pengembang

**Muhammad Raihan Rizky Zain**
- NIM: 140810230049
- Program Studi: Teknik Informatika
- Mata Kuliah: Artificial Intelligence
- Universitas: [Nama Universitas]

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik dalam mata kuliah Artificial Intelligence.

## 🙏 Acknowledgments

- Terima kasih kepada dosen dan asisten mata kuliah AI
- Dokumentasi Streamlit dan scikit-learn
- Community Python Indonesia

---

**Catatan**: Aplikasi ini dibuat sebagai tugas praktikum dan dapat dikembangkan lebih lanjut sesuai kebutuhan.
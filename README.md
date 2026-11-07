# 🩺 Aplikasi Prediksi Risiko Diabetes

Aplikasi web interaktif berbasis **Machine Learning** untuk memprediksi tingkat risiko penyakit diabetes berdasarkan data medis, hasil laboratorium, dan gaya hidup pasien.

> Dibangun menggunakan **Python**, **Scikit-Learn (Random Forest Classifier)**, dan **Streamlit**.

---

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem prediksi risiko diabetes menggunakan algoritma **Random Forest Classifier**. Pengguna cukup memasukkan data kesehatan melalui antarmuka web, dan model ML akan menghitung probabilitas risiko diabetes secara real-time.

### Fitur Utama:
- ✅ Prediksi risiko diabetes dengan **probabilitas persentase**
- ✅ Antarmuka web interaktif menggunakan **Streamlit**
- ✅ Tampilan **3 kolom sejajar (wide layout)** yang responsif dan rapi
- ✅ Kalkulasi **BMI otomatis** berdasarkan tinggi & berat badan
- ✅ Indikator visual status risiko (**Rendah** vs **Tinggi**)

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
| :--- | :--- |
| **Python 3.11** | Bahasa pemrograman utama |
| **Pandas & NumPy** | Manipulasi dan pemrosesan data |
| **Scikit-Learn** | Algoritma ML (Random Forest), StandardScaler, Evaluasi Model |
| **Streamlit** | Framework antarmuka web interaktif |
| **Pickle** | Serialisasi model dan artefak ML |

---

## 📂 Struktur Proyek

```
diabetes-risk-app/
│
├── app.py                          # Aplikasi web Streamlit (file utama)
├── diabetes_model.pkl              # Model ML (Random Forest Classifier)
├── diabetes_scaler.pkl             # StandardScaler untuk normalisasi fitur
├── diabetes_columns.pkl            # Daftar kolom fitur setelah One-Hot Encoding
├── diabetes_kolom_kategorikal.pkl  # Daftar kolom kategorikal
├── requirements.txt                # Dependensi library Python
```

---

## ⚙️ Cara Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/diabetes-risk-app.git
cd diabetes-risk-app
```

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada alamat `http://localhost:8501`.

---

## 📊 Fitur Input Data

Aplikasi menerima **35 variabel input** yang terbagi dalam 3 kategori:

### 👤 Profil Fisik & Vital
| Input | Tipe |
| :--- | :--- |
| Umur | Numerik |
| Jenis Kelamin | Kategorikal (Male / Female / Other) |
| Negara | Kategorikal (Indonesia / Malaysia / Japan / United States) |
| Tinggi Badan (cm) | Numerik |
| Berat Badan (kg) | Numerik |
| BMI | Otomatis dihitung |
| Tekanan Darah Sistolik & Diastolik | Numerik |
| Detak Jantung (bpm) | Numerik |
| Tipe Pekerjaan | Kategorikal |
| Tipe Tempat Tinggal | Kategorikal (Urban / Rural) |

### 🩸 Hasil Laboratorium & Darah
| Input | Tipe |
| :--- | :--- |
| Glukosa Darah (mg/dL) | Numerik |
| HbA1c (%) | Numerik |
| Gula Darah Puasa (mg/dL) | Numerik |
| Kadar Insulin | Numerik |
| Total Kolesterol, HDL, LDL | Numerik |
| Trigliserida | Numerik |
| Konsumsi Gula | Kategorikal (Low / Moderate / High) |
| Kepatuhan Obat | Kategorikal (Good / Poor / Unknown) |

### 🏃 Gaya Hidup & Riwayat Medis
| Input | Tipe |
| :--- | :--- |
| Tingkat Aktivitas Fisik | Kategorikal (Low / Moderate / High) |
| Olahraga (Jam/Minggu) | Numerik |
| Jalan Kaki (Menit/Hari) | Numerik |
| Jam Tidur / Hari | Numerik |
| Konsumsi Air (Liter/Hari) | Numerik |
| Kualitas Diet | Kategorikal (Healthy / Poor) |
| Tingkat Stres | Kategorikal |
| Status Merokok | Kategorikal (Never / Former / Current) |
| Konsumsi Alkohol | Kategorikal (Never / Occasionally / Daily) |
| Riwayat Diabetes Keluarga | Yes / No |
| Hipertensi | Yes / No |
| Penyakit Jantung | Yes / No |
| Fatty Liver | Yes / No |
| PCOS | Yes / No |

---

## 🧠 Alur Kerja Machine Learning

```
Dataset CSV
    ↓
Exploratory Data Analysis (EDA)
    ↓
Preprocessing (One-Hot Encoding + StandardScaler)
    ↓
Train-Test Split (80:20)
    ↓
Training Model (Random Forest Classifier)
    ↓
Evaluasi (Accuracy, Precision, Recall, F1-Score)
    ↓
Export Artefak (.pkl)
    ↓
Deploy ke Streamlit Web App
```

---

## 📈 Hasil Output Prediksi

Setelah pengguna mengisi data dan menekan tombol **"Jalankan Prediksi"**, aplikasi akan menampilkan:

- **Status Risiko**: `RISIKO RENDAH DIABETES` atau `RISIKO TINGGI DIABETES`
- **Skor Probabilitas**: Persentase kemungkinan risiko diabetes (0% - 100%)
- **Progress Bar**: Visualisasi indikator probabilitas risiko

---

## 📝 Catatan

- Model ML dilatih menggunakan **Google Colab** dan diekspor dalam format `.pkl`.
- Pastikan versi `scikit-learn` yang digunakan kompatibel dengan versi saat model dilatih.
- Aplikasi ini dibuat untuk tujuan **edukasi dan pembelajaran**, bukan untuk diagnosis medis profesional.

---

## 👤 Author

**Zikri Azzuri**

---

## 📄 License

Proyek ini bersifat open-source untuk keperluan edukasi dan pembelajaran.

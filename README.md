🏝️ Profil Liburan Bali Kamu:

Aplikasi kuis interaktif berbasis Streamlit untuk menentukan gaya liburan kamu di Bali berdasarkan preferensi kendaraan, akomodasi, destinasi, dan kebiasaan digital. Hasil kuis akan divisualisasikan dalam grafik kuadran seru:
Bapack/Emack – Kids Zaman Now dan Frugal – Sosialita.


🎯 Fitur Utama:

📋 Kuis interaktif dengan pertanyaan-pertanyaan pilihan ganda

🚗 Opsi kendaraan bensin atau listrik (termasuk gambar mobil)

🏨 Pilihan akomodasi, itinerary, dan gaya liburan

🧑‍🤝‍🧑 Multi-member: bisa input banyak nama dan profil

📊 Visualisasi hasil dalam grafik kuadran profil

🔁 Tombol reset quiz, reset profil terakhir, dan tambah member baru

🧪 Cara Menjalankan Aplikasi

Instalasi Python dan Streamlit:
pip install streamlit matplotlib
streamlit run ProgramBaliHoliday.py
Atau deploy langsung via Streamlit Cloud (bisa dari GitHub).

🧠 Cara Kerja Aplikasi
User memasukkan nama & umur

Menjawab pertanyaan kuis (otomatis menyesuaikan berdasarkan pilihan mobil listrik/bensin)

Jawaban memiliki bobot skor untuk dua sumbu:

X = Kids Zaman Now ←→ Bapack / Emack

Y = Frugal ←→ Sosialita

Hasil plotting berupa posisi pengguna pada grafik kuadran.

Bisa menambah member lain atau reset hasil sebelumnya.

📂 Struktur Folder (jika digunakan di GitHub)
bash
Copy
Edit
.
├── app.py
├── README.md
├── /images
│   ├── airev.avif
│   ├── byd.jpg
│   ├── brio.webp
│   └── ...
Semua gambar mobil dan destinasi diambil dari repo GitHub menggunakan URL mentah (raw.githubusercontent.com)

📌 Contoh Kuadran
markdown
              ↑ Sosialita
              |
Kids Zaman Now <-- | --> Bapack / Emack
              |
          ↓ Frugal
🙌 Kontribusi
Jika kamu ingin menambahkan pertanyaan, opsi baru, atau ide pengembangan (seperti penyimpanan hasil atau share di sosial media), feel free untuk fork dan pull request ya!

👨‍💻 Dibuat oleh
Yosafat Hans Wijaya – sebagai bagian dari eksperimen interaktif menggunakan Streamlit.

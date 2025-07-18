import streamlit as st
import matplotlib.pyplot as plt

#Title
st.title("Profil Liburan Bali Kamu")
st.image("https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/welcometobali.jpg")
# Deskripsi
st.header("Selamat datang aplikasi penentuan profil berdasarkan pilihan-pilihan kamu di Bali!")

#Input Member
if "members" not in st.session_state:
    st.session_state["members"] = []

if "last_plotted" not in st.session_state:
    st.session_state["last_plotted"] = False

# Declare a variable to store the score on X and Y axis
# X= Kids Zaman Now - Bapack / Emack
# Y= Frugal - Sosialita
scorex = 0
scorey = 0


# Input teks, jenis kelamin, dan umur
name = st.text_input("Masukkan Nama Kamu", "Nama Kamu", key="name")
age = st.number_input("Masukkan Umur Kamu (min 0 tahun max 100 tahun)", min_value=1, max_value=100,key="age")

# Input pilihan mobil listrik / bensin 
datasoal_A = [
    {"question": "Kamu suka sewa mobil bensin atau listrik dan kenapa?",
        "options": [
            "Mobil Listrik, biar keren",
            "Mobil Listrik, biar keluar, nyaman dan halus buat keluarga",
            "Mobil Bensin, murah biaya sewanya",
            "Mobil Bensin, takut lupa charge"],
"answer_weights":  {
            "Mobil Listrik, biar keren": {"scorex": -0.5, "scorey": +0.5, "vehicle_type": "listrik"}, 
            "Mobil Listrik, biar keluar, nyaman dan halus buat keluarga": {"scorex": +0.5, "scorey": +0.5, "vehicle_type": "listrik"}, 
            "Mobil Bensin, murah biaya sewanya": {"scorex": +0.5, "scorey": -0.5, "vehicle_type": "bensin"}, 
            "Mobil Bensin, takut lupa charge": {"scorex": -0.5, "scorey": -0.5, "vehicle_type": "bensin"}}
}]

# Tarik jawaban soal_A
jawaban = []
for i, q in enumerate(datasoal_A):
    st.subheader(f"{i+1}. {q['question']}")
    selected = st.radio("Pilih salah satu:", q["options"], key=f"q{i}")
    weights = q["answer_weights"].get(selected, {})
    jawaban.append((selected, weights))
    scorex += weights.get("scorex", 0)
    scorey += weights.get("scorey", 0)

# Cek soal Jenis Kendaraan
if "vehicle_type" in weights:
    st.session_state["vehicle_type"] = weights["vehicle_type"]

if st.session_state.get("vehicle_type") == "listrik": 
    datasoal_Ax = [
        {
            "question": "Mau sewa mobil listrik apa?",
            "options": [
            "Wuling AirEV",
            "BYD M6",
            "Denza D9",
            "Hyundai New Kona",
        ],
            "image": [
                "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/airev.avif",
                "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/byd.jpg",
                "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/denza.webp",
                "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/kona.webp"
                ],

            "answer_weights": {
            "Wuling AirEV":{"scorex":-0.5,"scorey":-0.5}, 
            "BYD M6":{"scorex":+0.5,"scorey":-0.5}, 
            "Hyundai New Kona": {"scorex":-0.5,"scorey":+0.5}, 
            "Denza D9":{"scorex":+0.5,"scorey":+0.5},

        }},
        {
            "question": "Listrik mobil habis, mau isi di mana?",
            "options":   ["Dealer / Bengkel Resmi aja biar gratis", 
            "Fast Charging Station, biar cepet"], 
            "image": [],
            "answer_weights": {
                "Dealer / Bengkel Resmi aja biar gratis": {"scorey": -0.5}, 
            "Fast Charging Station, biar cepet": {"scorey": +0.5}
            }
        }    
    ]
elif st.session_state.get("vehicle_type") == "bensin": 
    datasoal_Ax= [
        {
        "question": "Mau sewa mobil bensin apa",
        "options": [
            "Honda Brio",
            "Suzuki Ertiga",
            "BMW 330i",
            "Toyota Alphard"
            
        ],
        "image": [
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/brio.webp",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/ertiga.jpeg",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/bmw.webp",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/alphard.avif"
        ],
        "answer_weights":{"Honda Brio": {"scorex": -0.5, "scorey": -0.5},
            "Suzuki Ertiga": {"scorex": +0.5, "scorey": -0.5},
            "BMW 330i": {"scorex": -0.5, "scorey": +0.5},
            "Toyota Alphard": {"scorex": +0.5, "scorey": +0.5}
        }},
        {
        "question": "Bensin mobil habis, mau isi bensin apa?",
        "options": [
            "BBM Subsidi aja lah",
            "BBM Non Subsidi biar aman dan kencang"
        ],
        "image": [],
        "answer_weights": {
            "BBM Subsidi aja lah": {"scorey": -0.5},
            "BBM Non Subsidi biar aman dan kencang": {"scorey": +0.5}
        }}]
    
# Tarik jawaban soal_Ax
offset1 = len(datasoal_A)
for i, q in enumerate(datasoal_Ax):
    st.subheader(f"{i+1+offset1}. {q['question']}")
    col1, col2 = st.columns([3, 4])
    with col1:
        selected = st.radio("Pilih salah satu:", q["options"], key=f"q{i+offset1}")
    with col2:
        images = st.image(q["image"], width=200)
    
    weights = q["answer_weights"].get(selected, {})
    jawaban.append((selected, weights))
    scorex += weights.get("scorex", 0)
    scorey += weights.get("scorey", 0)

# Input pilihan liburan 2
datasoal_B = [
        {
        "question": "Sewa sama pengemudi atau lepas kunci?",
        "options": [
            "Pengemudi, mau sambil ngonten",
            "Pengemudi, biar bisa deeptalk sama keluarga",
            "Lepas kunci, bisa dipakai yang lain duitnya",
            "Lepas kunci, pengen bebas explore sendiri"
        ],
        "image": [],
        "answer_weights": {
            "Pengemudi, mau sambil ngonten": {"scorex": -0.5, "scorey": +0.5},
            "Pengemudi, biar bisa deeptalk sama keluarga": {"scorex": +0.5, "scorey": +0.5},
            "Lepas kunci, bisa dipakai yang lain duitnya": {"scorex": +0.5, "scorey": -0.5},
            "Lepas kunci, pengen bebas explore sendiri": {"scorex": -0.5, "scorey": -0.5}
        }},
        {
        "question": "Mau nginap di mana?",
        "options": [
            "Hotel strategis asal bersih terawat",
            "Hotel strategis yang mewah dan hit spot di medsos",
            "Villa milik warlok / bule",
            "Villa di tengah resort dari jaringan hotel internasional"
        ],
        "image": [],
        "answer_weights": {
            "Hotel strategis asal bersih terawat": {"scorex": -0.5, "scorey": -0.5},
            "Hotel strategis yang mewah dan hit spot di medsos": {"scorex": -0.5, "scorey": +0.5},
            "Villa milik warlok / bule": {"scorex": +0.5, "scorey": -0.5},
            "Villa di tengah resort dari jaringan hotel internasional": {"scorex": +0.5, "scorey": +0.5}
        }
        },
        {
        "question": "Destinasi impian / wajib kamu?",
        "options": [
            "Kuta atau Sanur",
            "Seminyak atau Canggu",
            "Ubud",
            "Kintamani atau Bedugul"
        ],
        "image": [
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/sanur.jpg",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/canggu.jpg",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/ubud.webp",
            "https://raw.githubusercontent.com/yosafathw/HolidayQuest/refs/heads/main/Assets/bedugul.jpg"
            ],
        "answer_weights": {
            "Kuta atau Sanur": {"scorex": -0.5, "scorey": -0.5},
            "Seminyak atau Canggu": {"scorex": -0.5, "scorey": +0.5},
            "Ubud": {"scorex": +0.5, "scorey": +0.5},
            "Kintamani atau Bedugul": {"scorex": +0.5, "scorey": -0.5}
        }
        },
        {
        "question": "Kamu lagi kehabisan ide itinerary, mau minta saran ke siapa?",
        "options": [
            "Tanya orang yang baru dikenal di tempat wisata sebelumnya",
            "Cek di google atau gmaps",
            "Cek di Instagram atau TikTok",
            "Tanya rekan bisnis yang pernah ke Bali"
        ],
        "image": [],
        "answer_weights": {
            "Tanya orang yang baru dikenal di tempat wisata sebelumnya": {"scorex": +0.5, "scorey": -0.5},
            "Cek di google atau gmaps": {"scorex": -0.5, "scorey": -1},
            "Cek di Instagram atau TikTok": {"scorex": -0.5, "scorey": +0.5},
            "Tanya rekan bisnis yang pernah ke Bali": {"scorex": +0.5, "scorey": +0.5},
        }
        },
        {
        "question": "Lagi lapar, makan di mana ya?",
        "options": [
            "Warung makan khas, nasi pedas or tempong gitu",
            "Restoran keluarga yang banyak dikunjungi turis",
            "Cafe estetik yang lagi hits di Instagram",
            "Gofood, makan sambil guyub bareng keluarga di villa"
        ],"image": [],
        "answer_weights": {            
            "Warung makan khas, nasi pedas or nasi tempong gitu": {"scorex": -0.5, "scorey": -0.5},
            "Restoran keluarga yang banyak dikunjungi turis": {"scorex": +0.5, "scorey": +0.5},
            "Cafe estetik yang lagi hits di Instagram": {"scorex": -0.5, "scorey": +0.5},
            "Gofood, makan sambil guyub bareng keluarga di villa": {"scorex": +0.5, "scorey": -0.5}
        }
        }
        ]

# Tarik jawaban soal_B
offset2 = len (datasoal_A) + len (datasoal_Ax)
for i, q in enumerate(datasoal_B):
    st.subheader(f"{i+1+offset2}. {q['question']}")
    col1, col2 = st.columns([3, 4])
    with col1:
        selected = st.radio("Pilih salah satu:", q["options"], key=f"q{i+offset2}")
    with col2:
        images = st.image(q["image"], width=200)
    jawaban.append((selected, q["answer_weights"].get(selected, {})))    

# Update score dari pengguna
    weights = q["answer_weights"].get(selected, {})
    jawaban.append((selected, weights))
    scorex += weights.get("scorex", 0)
    scorey += weights.get("scorey", 0)

# Tampilkan tombol Profil / Plot
if st.button("Lihat Hasil Profil Liburan Saya"):
    if not jawaban or not all(isinstance(w, tuple) for w in jawaban):
        st.error("Harap isi semua pertanyaan terlebih dahulu.")
        st.stop()
    else:
        if not name or not isinstance(age, int):
            st.error("Nama dan umur wajib diisi dengan benar.")
            st.stop()
        else:
            if st.session_state.get("last_plotted", False):
                st.warning("Profil terakhir sudah ditambahkan ke grafik. Reset dulu profil terakhir jika ingin mengubah pilihan.")
            else:
                st.session_state["last_plotted"] = True
                scorex = 0
                scorey = 0
                if age <= 22:
                    scorex -= 1
                elif age <= 30:
                    scorex -= 0.5
                elif age <= 35:
                    scorex += 0
                elif age <= 45:
                    scorex += 0.5
                else:
                    scorex += 1
                # Masukkan Score Dari Jawaban
                for _, weights in jawaban:
                    scorex += weights.get("scorex", 0)
                    scorey += weights.get("scorey", 0)
                # Member Tambah
                st.session_state["members"].append({
                "name": name,
                "scorex": scorex,
                "scorey": scorey
                })
            # Masukkan ke Plot
            fig, ax = plt.subplots(figsize=(6.5, 6.5))
            # Garis-Garis
            ax.axhline(0, color='gray', linestyle='--')
            ax.axvline(0, color='gray', linestyle='--')
            # Titik User
            for m in st.session_state["members"]:
                ax.scatter(m["scorex"], m["scorey"], s=100, label=m["name"])
                ax.text(m["scorex"] + 0.2, m["scorey"] + 0.2, m["name"], fontsize=10)
            # Nama Kuadran
            ax.text(6, -6, "Bapack-Emack\nFrugal", fontsize=10, ha='center', va='center')
            ax.text(6, 6, "Bapack-Emack\nSosialita", fontsize=10, ha='center', va='center')
            ax.text(-6, -6, "Kids Zaman Now\nFrugal", fontsize=10, ha='center', va='center')
            ax.text(-6, 6, "Kids Zaman Now\nSosialita", fontsize=10, ha='center', va='center')
            # Set limits and titles
            ax.set_xlim(-6.5, 6.5)
            ax.set_ylim(-6.5, 6.5)
            ax.set_xlabel("Kids Zaman Now  →  Bapack / Emack")
            ax.set_ylabel("Frugal  →  Sosialita")
            ax.set_title("Profil Liburan Bali Kamu")
            # Remove ticks
            ax.set_xticks([])
            ax.set_yticks([])
            # Display in Streamlit
            st.pyplot(fig)

# Buttons Layout
col1, col2, col3 = st.columns(3)
with col1:
    tambah_clicked = st.button("Tambah Member Baru", key="add_member_btn")
with col2:
    reset_clicked = st.button("Ulangi / Reset Quiz", key="reset_quiz_btn")
with col3:
    profil_clicked = st.button("Reset Profil Terakhir", key="profil_quiz_btn")

# Buttons Logic
if reset_clicked:
    for key in list(st.session_state.keys()):
        if key.startswith("q") or key in ["scorex", "scorey", "name", "age", "members","vehicle_type","last_plotted"]:
            del st.session_state[key]
    st.rerun()
elif tambah_clicked:
    st.session_state["last_plotted"] = False
    st.rerun()
elif profil_clicked: 
    if st.session_state.get("members"):
        st.session_state["members"].pop()
        st.session_state["last_plotted"] = False
        st.rerun()


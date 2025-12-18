import streamlit as st

# Data Menu/Variabel
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Es Teh": 5000,
    "Es Jeruk": 7000,
    "Kopi": 8000
}

# Fungsi untuk menghitung total harga
def hitung_total(pesanan):
    """Menghitung total harga dari pesanan"""
    total = 0
    for item in pesanan:
        total += item["harga"]
    return total


# Inisialisasi session state
if "pesanan" not in st.session_state:
    st.session_state.pesanan = []

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "nama" not in st.session_state:
    st.session_state.nama = ""

if "meja" not in st.session_state:
    st.session_state.meja = ""


# hal utama aplikasi
st.title("Aplikasi Pemesanan Makanan & Minuman")

# sidebar menu
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Data Pembeli",
        "Pemesanan Makanan",
        "Pemesanan Minuman",
        "Checkout & Riwayat"
    ]
)

# data pembeli
if menu == "Data Pembeli":
    st.header("👤 Data Pembeli")

    st.session_state.nama = st.text_input("Nama Pembeli")
    st.session_state.meja = st.text_input("Nomor Meja")

    if st.session_state.nama and st.session_state.meja:
        st.success("Data pembeli berhasil disimpan")

# Pemesanan Makanan
elif menu == "Pemesanan Makanan":
    st.header("🍛 Pemesanan Makanan")

    pilihan = st.selectbox("Pilih Makanan", list(menu_makanan.keys()))
    harga_satuan = menu_makanan[pilihan]

    st.info(f"Harga satuan: Rp {harga_satuan:,}")

    jumlah = st.number_input("Jumlah", min_value=1, step=1)
    total_sementara = harga_satuan * jumlah

    st.write(f"Total harga: Rp {total_sementara:,}")

    if st.button("Tambah ke Pesanan"):
        st.session_state.pesanan.append({
            "nama": pilihan,
            "jumlah": jumlah,
            "harga": total_sementara
        })
        st.success("Makanan berhasil ditambahkan")

# Pemesanan Minuman
elif menu == "Pemesanan Minuman":
    st.header("🥤 Pemesanan Minuman")

    pilihan = st.selectbox("Pilih Minuman", list(menu_minuman.keys()))
    harga_satuan = menu_minuman[pilihan]

    st.info(f"Harga satuan: Rp {harga_satuan:,}")

    jumlah = st.number_input("Jumlah", min_value=1, step=1)
    total_sementara = harga_satuan * jumlah

    st.write(f"Total harga: Rp {total_sementara:,}")

    if st.button("Tambah ke Pesanan"):
        st.session_state.pesanan.append({
            "nama": pilihan,
            "jumlah": jumlah,
            "harga": total_sementara
        })
        st.success("Minuman berhasil ditambahkan")

# Checkout & Riwayat
elif menu == "Checkout & Riwayat":
    st.header("🧾 Checkout Pesanan")

    if not st.session_state.nama or not st.session_state.meja:
        st.warning("Silakan isi Data Pembeli terlebih dahulu")
    elif len(st.session_state.pesanan) == 0:
        st.info("Belum ada pesanan aktif")
    else:
        st.write(f"**Nama Pembeli:** {st.session_state.nama}")
        st.write(f"**Nomor Meja:** {st.session_state.meja}")
        st.divider()

        for i, item in enumerate(st.session_state.pesanan, start=1):
            st.write(
                f"{i}. {item['nama']} x {item['jumlah']} = Rp {item['harga']:,}"
            )

        total = hitung_total(st.session_state.pesanan)
        st.divider()
        st.subheader(f"💰 Total Bayar: Rp {total:,}")

        if st.button("Checkout"):
            st.session_state.riwayat.append({
                "nama": st.session_state.nama,
                "meja": st.session_state.meja,
                "pesanan": st.session_state.pesanan.copy(),
                "total": total
            })
            st.session_state.pesanan = []
            st.success("Pesanan berhasil disimpan ke riwayat")

# Riwayat Pesanan
    st.divider()
    st.header("📜 Riwayat Pesanan")

    if len(st.session_state.riwayat) == 0:
        st.info("Belum ada riwayat pesanan")
    else:
        for i, data in enumerate(st.session_state.riwayat, start=1):
            st.subheader(f"Pesanan ke-{i}")
            st.write(f"Nama: {data['nama']}")
            st.write(f"Meja: {data['meja']}")

            for item in data["pesanan"]:
                st.write(
                    f"- {item['nama']} x {item['jumlah']} = Rp {item['harga']:,}"
                )

            st.write(f"**Total: Rp {data['total']:,}**")
            st.divider()


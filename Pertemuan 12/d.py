import streamlit as st
# Fungsi untuk menghitung luas bangun datar
def persegi(sisi):
    return sisi * sisi

def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def lingkaran(jari2):
    return 3.14 * jari2 * jari2

# Halaman Utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.title('Buatan anak SI')

# Sidebar navigasi
menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran'])

if menu == 'Luas Persegi':
    st.subheader('Hitung Luas Persegi')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ4dJ9QMK_50OUPJNELw3AbynuL1f33ESOSq_nlFi-gnMIA4SMDvJ8Vy39NcxfWGqlv2Bn6EiIFlGm2rLw4xxmYTMD3wL85mgXggy86WRuR02OYSCKWbCIUyjOI88dCwKMctfLj3txfNM/s1600/rumus-luas-persegi-dan-keliling-persegi.JPG",
        caption="Ilustrasi Persegi",
        width=300,
    )

    # Input sisi
    input_sisi = st.number_input('silahkan Masukkan Sisi', min_value=0)
    if st.button('Hitung Luas Persegi'):
        if input_sisi > 0:
            luas = persegi(input_sisi)
            st.write(f"Luas persegi adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai sisi yang lebih besar dari 0!')

elif menu == 'Luas Segitiga':
    st.subheader('Hitung Luas Segitiga')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvnU93yw54EG4p3cL7lMuWFeCGlkPv0co7cA&s",
        caption="Ilustrasi Segitiga",
        width=300,
    )

    # Input Data
    input_alas = st.number_input('Masukkan Alas', min_value=0.0)
    input_tinggi = st.number_input('Masukkan Tinggi', min_value=0.0)

    if st.button('Hitung Luas Segitiga'):
        if input_alas > 0 and input_tinggi > 0:
            luas = segitiga(input_alas, input_tinggi)
            st.write(f"Luas segitiga adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai alas dan tinggi yang lebih besar dari 0!')

elif menu == 'Luas Lingkaran':
    st.subheader('Hitung Luas Lingkaran')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253bd91b52f8-rumus-luas-lingkaran_1265_711.jpg",
        caption="Ilustrasi Lingkaran",
        width=300,
    )

    # Input Data
    input_jari2 = st.number_input('Masukkan Jari-Jari', min_value=0.0)

    if st.button('Hitung Luas Lingkaran'):
        if input_jari2 > 0:
            luas = lingkaran(input_jari2)
            st.write(f"Luas lingkaran adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai jari-jari yang lebih besar dari 0!')

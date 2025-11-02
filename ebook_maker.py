import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Ebook Maker", layout="wide")

st.title("📘 AI Ebook Maker")
st.markdown("Buat eBook otomatis menggunakan kecerdasan buatan.")

# Sidebar Config
st.sidebar.header("Langkah 1: Konfigurasi Ebook")

api_key = st.sidebar.text_input("Masukkan OpenAI API Key", type="password")
masalah = st.sidebar.text_area("Jelaskan Masalah Anda", "Saya sulit capai 10 juta pertama dari jualan eBook")
gaya_bahasa = st.sidebar.selectbox("Pilih Gaya Bahasa", ["Profesional", "Santai", "Serius", "Inspiratif", "Akademis"])
jumlah_bab = st.sidebar.number_input("Jumlah Bab Awal", 1, 10, 3)

if st.sidebar.button("Buat Ebook"):
    if not api_key:
        st.error("Masukkan API Key terlebih dahulu.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            prompt = f"""
            Buatkan eBook lengkap dengan {jumlah_bab} bab.
            Gaya bahasa: {gaya_bahasa}.
            Topik utama: {masalah}.
            Tulis dengan struktur eBook yang rapi dan mudah dibaca.
            """

            with st.spinner("Sedang membuat eBook..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

            hasil = response.choices[0].message.content
            st.subheader("📖 Isi eBook Anda")
            st.markdown(hasil)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

import streamlit as st
from openai import OpenAI

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="AI Ebook Maker", layout="wide")

st.title("📘 AI Ebook Maker")
st.markdown("Buat eBook otomatis menggunakan kecerdasan buatan.")

# --- Langkah 1: Konfigurasi ---
st.sidebar.header("Langkah 1: Konfigurasi Ebook")

api_key = st.sidebar.text_input("Masukkan OpenAI API Key", type="password")
masalah = st.sidebar.text_area("Jelaskan Masalah Anda", "saya sulit capai 10 juta pertama dari jualan ebook")
gaya_bahasa = st.sidebar.selectbox("Pilih Gaya Bahasa", 
                                   ["Profesional", "Santai", "Serius", "Inspiratif", "Akademis"])
jumlah_bab = st.sidebar.number_input("Jumlah Bab Awal", 1, 10, 3)

# --- Tombol untuk Generate Ebook ---
if st.sidebar.button("Buat Ebook"):
    if not api_key:
        st.error("Masukkan OpenAI API Key terlebih dahulu.")
    else:
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Buatkan eBook lengkap dengan {jumlah_bab} bab.
        Gaya bahasa: {gaya_bahasa}.
        Topik atau masalah utama: {masalah}.
        Tulis dengan struktur yang rapi, menarik, dan mudah dibaca.
        """

        with st.spinner("Sedang membuat eBook..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

        hasil = response.choices[0].message.content
        st.subheader("📖 Isi Ebook Anda")
        st.write(hasil)
st.download_button("💾 Unduh eBook (TXT)", hasil)

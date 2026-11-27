import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout='wide')

st.markdown('<h1 style="font-family: Arial, sans-serif; font-size: 36px; color: #FF9900; text-align: center;">Kriminalitas Indonesia</h1>', unsafe_allow_html=True)

import streamlit as st

data_1 = pd.read_csv('kriminal_2023.csv')
data_2 = pd.read_csv('kriminal_2022.csv')
data_3 = pd.read_csv('kriminal_2021.csv')

# Menu Sidebar
st.sidebar.title('Menu')
st.sidebar.markdown('---')
menu_options = ['📊 Summary', '2021 📅', '2022 📅', '2023 📅']
selected_menu = st.sidebar.radio('', menu_options)

# Konten berdasarkan pilihan menu
if selected_menu == '📊 Summary':
    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Pengertian Kriminalitas</p></p></p>', unsafe_allow_html=True)

    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">Kriminalitas merujuk pada perilaku yang melanggar hukum atau tindakan yang dianggap ilegal dalam suatu masyarakat atau negara. Ini mencakup berbagai jenis kejahatan seperti pembunuhan, pencurian, pemerkosaan, penipuan, perampokan, narkotika, dan banyak lagi. Kriminalitas dapat melibatkan tindakan fisik, seperti kekerasan atau merampok, atau tindakan non-fisik, seperti penipuan melalui internet atau pemalsuan dokumen. Berikut merupakan rangkuman sederhana tentang data kriminalitas berdasarkan Badan Pusat Statistik dalam kurun waktu 2019-2023. </p>', unsafe_allow_html=True)

    img = Image.open("Total Kasus Per Tahun.png")
    st.image(img, caption="Gambar1", width = 750)

    # Menampilkan deskripsi teks tanpa "with Description:"
    st.write(
    '<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify; color: #000;">'
    'Jumlah kejahatan menurun dari 2019 hingga 2021, lalu melonjak tajam pada 2022 dan 2023.'
    '</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Penyelesaian Kriminalitas Dalam Kurun Waktu 5 Tahun</p></p></p>', unsafe_allow_html=True)

    # Membuat data frame dalam format long

    img = Image.open("Avg kasus selesai.png")
    st.image(img, caption="Gambar2", width = 1500)

    
    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">DI Yogyakarta memiliki tingkat penyelesaian kasus tertinggi (83,72%), sedangkan Papua Barat terendah (27,87%).', unsafe_allow_html=True)

    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Tipe Kasus Kriminalitas</p></p></p>', unsafe_allow_html=True)
  
    img = Image.open("Tipe Total Kasus .png")
    st.image(img, caption="Gambar3", width = 1600)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">Jenis kejahatan terbanyak adalah narkotika dan psikotropika (180.959 kasus), sedangkan korupsi memiliki jumlah kasus terendah (1.860 kasus). </p>', unsafe_allow_html=True)
  
elif selected_menu == '2021 📅':
    st.header('Tahun : 2021')
    mx_crime, mx_rate = st.columns(2)

    with mx_crime:
        jlh_kasus1 = data_3['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus1)  # Format dengan pemisah ribuan
        
    
    # Menampilkan metrik
        st.metric('Jumlah Kasus', jlh_kasus_formatted)
  
    img = Image.open("2021.png")
    st.image(img, width = 3000)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">Pada Tahun 2021 polda dengan jumlah kriminalitas tertinggi pada tahun 2021 adalah Sumatera Utara (36.534 kasus).</p>',unsafe_allow_html=True)
    

elif selected_menu == '2022 📅':
    st.header('Tahun : 2022')
    mx_crime_1, mx_rate_1  = st.columns(2)

    with mx_crime_1:
        jlh_kasus2 = data_2['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus2)  # Format dengan pemisah ribuan
    
    # Menghitung persentase perubahan
        prev_value = 239481 # Nilai sebelumnya
        current_value = jlh_kasus2 # Nilai sekarang
        diff = current_value - prev_value  # Selisih
        diff_pct = (diff / prev_value) * 100  # Persentase perubahan
    
    # Menentukan label persentase (positif untuk kenaikan, negatif untuk penurunan)
        if diff >= 0:
            diff_pct_formatted = '{:.2f}%'.format(diff_pct)  # Jika naik
            comment = "Menunjukkan peningkatan sebesar 55,74% dibandingkan dengan tahun 2021 yang hanya mencatatkan 239,481 kasus."  # Komentar jika naik
        else:
            diff_pct_formatted = '{:.2f}%'.format(diff_pct)  # Jika turun
            comment = "Jumlah kasus menurun."  # Komentar jika turun
    
    # Menampilkan metrik
        st.metric('Jumlah Kasus', jlh_kasus_formatted, f'+{diff_pct_formatted}' if diff >= 0 else f'{diff_pct_formatted}')
        st.write(comment)  # Menampilkan komentar

    img = Image.open("2022.png")
    st.image(img, width = 3000)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">Pada Tahun 2022 polda dengan jumlah kriminalitas tertinggi adalah Jawa Timur (51.905 kasus).</p>', unsafe_allow_html=True)
    

elif selected_menu == '2023 📅':
    st.header('Tahun : 2023')
    mx_crime, mx_rate = st.columns(2)

    with mx_crime:
        jlh_kasus3 = data_1['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus3)  # Format dengan pemisah ribuan
    
    # Menghitung persentase perubahan
        prev_value = 372965  # Nilai sebelumnya
        current_value = 584911 # Nilai sekarang
        diff = current_value - prev_value  # Selisih
        diff_pct = (diff / prev_value) * 100  # Persentase perubahan
    
    # Menentukan label persentase (positif untuk kenaikan, negatif untuk penurunan)
        if diff >= 0:
            diff_pct_formatted = '{:.2f}%'.format(diff_pct)  # Jika naik
            comment = "Menunjukan peningkatan sebesar 55,93% dibandingkan dengan tahun 2022 yang hanya mencatatkan 372.965 kasus." 
        else:
            diff_pct_formatted = '{:.2f}%'.format(diff_pct)  # Jika turun
            comment = "Jumlah kasus menurun."  # Komentar jika turun
    
    # Menampilkan metrik
        st.metric('Jumlah Kasus', jlh_kasus_formatted, f'+{diff_pct_formatted}' if diff >= 0 else f'{diff_pct_formatted}')
        st.write(comment)  # Menampilkan komentar


    img = Image.open("2023.png")
    st.image(img, width = 3000)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 20px; text-align: justify;">Pada Tahun 2023 polda dengan jumlah kriminalitas tertinggi adalah Metro Jaya (87.426 kasus)</p>', unsafe_allow_html=True)
    








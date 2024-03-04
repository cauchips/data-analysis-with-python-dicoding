import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='dark')

all_df = pd.read_csv("main_data.csv")

with st.sidebar:
    st.image("https://placehold.co/600x400?text=Jonathan+Chandra")
    st.markdown("# Proyek Jonathan Chandra :sparkles:")

st.title('Dashboard Sepeda Berbagi')

st.header('Perbandingan Jumlah Rental Berdasarkan Musim antara Tahun 2011 dan 2012')
st.markdown('Atur tahun di sidebar! :smile:')
season_order = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']

selected_year = st.sidebar.selectbox("Pilih Tahun", all_df['yr'].unique())

total_rental_season = all_df[all_df['yr'] == selected_year].groupby(['season_indonesia'])['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=total_rental_season, x='season_indonesia', y='cnt', order=season_order)
plt.title(f'Jumlah Rental Berdasarkan Musim Pada Tahun {selected_year}')
plt.xlabel('Musim')
plt.ylabel('Jumlah Rental')
st.pyplot(plt)

st.header("Pengaruh Cuaca terhadap Perilaku Pengguna Rental")
weather_order = ['Cerah', 'Berawan/Berkabut', 'Hujan Ringan/Salju', 'Hujan Lebat/Berembun']
total_rental_weather = all_df.groupby(['dteday', 'weather_indonesia'])['cnt'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.boxplot(data=total_rental_weather, x='weather_indonesia', y='cnt', order=weather_order)
plt.title('Jumlah Rental Per Hari Berdasarkan Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Rental Per Hari')
st.pyplot(plt)

st.header("Perbandingan Jumlah Pengguna Terdaftar Berdasarkan Bulan antara Tahun 2011 dan 2012")
total_rental_monthly = all_df.groupby(['yr', 'month_indonesia'])['registered'].sum().reset_index()

month_order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

plt.figure(figsize=(12, 6))
sns.barplot(data=total_rental_monthly, x='month_indonesia', y='registered', hue='yr', order=month_order)
plt.title('Perbandingan Jumlah Pengguna Terdaftar Berdasarkan Bulan antara Tahun 2011 dan 2012')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Rental Pengguna Terdaftar')
plt.legend(title='Tahun')
plt.xticks(rotation=45)
st.pyplot(plt)

st.header("Distribusi Jumlah Rental Berdasarkan Hari Kerja dan Hari Libur dalam Setiap Musim")
st.markdown('Atur musim di sidebar! :smile:')

selected_season = st.sidebar.selectbox("Pilih Musim", all_df['season_indonesia'].unique())

is_workday = all_df[all_df['season_indonesia'] == selected_season].groupby(['workingday'])['cnt'].sum().reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(data=is_workday, x='workingday', y='cnt', hue='workingday')
plt.title(f'Distribusi Jumlah Rental di {selected_season}')
plt.xlabel('Hari Kerja')
plt.ylabel('Jumlah Rental')
plt.legend(title='Keterangan')
st.pyplot(plt)

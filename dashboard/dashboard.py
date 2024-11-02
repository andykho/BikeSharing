import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib
from scipy import stats
import streamlit as st

day_df = pd.read_csv('dashboard/day_dboard.csv')
hour_df = pd.read_csv('dashboard/hour_dboard.csv')

st.title("Bike Sharing")
st.sidebar.header("Filter Options")

# Sidebar year untuk sewa pada tahun 2011 dan 2012 , dan juga multiselect dropdown
years = day_df['year'].unique()
total_registered = day_df.groupby('year')['registered'].sum().values
total_casual = day_df.groupby('year')['casual'].sum().values

selected_years = st.sidebar.multiselect("Select year(s)", options=years, default=years)

# Sidebar hour untuk sewa berdasarkan jam , dan slider juga
hours = hour_df['hours'].unique()
rentals = hour_df['count_df'].values

hour_range = st.sidebar.slider("Select hour range", min_value=int(hours.min()), max_value=int(hours.max()), value=(int(hours.min()), int(hours.max())))

# visualisasi chart tahun 2011 dan 2012
st.subheader("Jumlah penyewaan sepeda tahun 2011 & 2012")

selected_registered = [total_registered[np.where(years == year)[0][0]] for year in selected_years if year in years]
selected_casual = [total_casual[np.where(years == year)[0][0]] for year in selected_years if year in years]
selected_x = np.arange(len(selected_years))

fig1, ax1 = plt.subplots()
bar_width = 0.3
ax1.bar(selected_x, selected_registered, width=bar_width, color="green", label='Registered')
ax1.bar(selected_x + bar_width, selected_casual, width=bar_width, color="yellow", label='Casual')
ax1.set_title('Total Penyewaan Sepeda')
ax1.set_xlabel('Year')
ax1.set_ylabel('Jumlah sewa')
ax1.set_xticks(selected_x + bar_width / 2)
ax1.set_xticklabels(selected_years)
ax1.legend()

for i in range(len(selected_years)):
    ax1.text(i, selected_registered[i] + 20000, selected_registered[i], ha='center', va='bottom')
    ax1.text(i + bar_width, selected_casual[i] + 20000, selected_casual[i], ha='center', va='bottom')

st.pyplot(fig1)

# visualisasi chart untuk penyewaan berdasarkan jam
st.subheader("Penyewaan Sepeda berdasarkan jam")

selected_hours = hours[hour_range[0]:hour_range[1] + 1]
selected_rentals = rentals[hour_range[0]:hour_range[1] + 1]

fig2, ax2 = plt.subplots()
ax2.plot(selected_hours, selected_rentals, marker='o', color='blue')
ax2.set_title('Penyewaan sepeda berdasarkan jam')
ax2.set_xlabel('Hour')
ax2.set_ylabel('Jumlah sewa')
ax2.grid(True)

st.pyplot(fig2)

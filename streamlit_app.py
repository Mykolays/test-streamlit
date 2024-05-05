import os
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.signal import butter, filtfilt

st.title("Solar Flare Analysis")

data_directory = os.path.abspath("./data")
filenames = os.listdir(data_directory)
filenames_no_extension = [os.path.splitext(filename)[0] for filename in filenames]


# st.sidebar.header("Cycle Choice")

selected_file = st.selectbox("Select cycle:", filenames_no_extension)


st.subheader(f"Analysis for {selected_file}")
df = pd.read_csv(f"Data/{selected_file}.csv")
with st.container():
    with st.container():
        f = px.line(
            df, 
            x="Data",
            y='T-day',
            title=f"Total index of {selected_file} daily"
        )
        st.plotly_chart(f)
    with st.container():
        f = px.line(
            df, 
            x="Data",
            y=['N-day', 'S minus'],
            title=f"{selected_file} N-S daily"
        )
        st.plotly_chart(f)
    with st.container():
        f = px.line(
            df, 
            x="Data",
            y=['S-day'],
            title=f"South index daily"
        )
        st.plotly_chart(f)
    with st.container():
        f = px.line(
            df, 
            x="Data",
            y=['N-day'],
            title=f"North index daily"
        )
        st.plotly_chart(f)
    
st.subheader("Wavelet Analysis for Selected Cycle")
photo_map = {
    'cycle_21-25': ['Wavelet_21-25_cycle_North.png', 'Wavelet_21-25_cycle_South.png', 'Wavelet_21-25_cycle_Total.png'],
    'cycle_21': ['Wavelet_21_cycle_North.png', 'Wavelet_21_cycle_South.png', 'Wavelet_21_cycle_Total.png'],
    'cycle_22': ['Wavelet_22_cycle_North.png', 'Wavelet_22_cycle_South.png', 'Wavelet_22_cycle_Total.png'],
    'cycle_23': ['Wavelet_23_cycle_North.png', 'Wavelet_23_cycle_South.png', 'Wavelet_23_cycle_Total.png'],
    'cycle_24': ['Wavelet_24_cycle_North.png', 'Wavelet_24_cycle_South.png', 'Wavelet_24_cycle_Total.png'],
    'cycle_25': ['Wavelet_25_cycle_North.png', 'Wavelet_25_cycle_South.png', 'Wavelet_25_cycle_Total.png']
}

photo_filenames = photo_map[selected_file]
for photo_filename in photo_filenames:
    photo_path = f"Data/wavelet/{photo_filename}"  # Assuming photos are in a 'photos' directory
    st.image(photo_path)

st.subheader("FFT Analysis for Selected Cycle")

# Perform FFT for 'T-day' column
t_day_fft = np.fft.fft(df['T-day'])
frequencies = np.fft.fftfreq(len(t_day_fft))

# Plot FFT
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:len(frequencies)//2], np.abs(t_day_fft)[:len(frequencies)//2])
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title(f"FFT of Total index of {selected_file} daily")
st.pyplot(plt)

# st.subheader("Bandpass Filtered FFT for Selected Cycle")
# # Define bandpass filter
# def butter_bandpass(lowcut, highcut, fs, order=5):
#     nyquist = 0.5 * fs
#     low = lowcut / nyquist
#     high = highcut / nyquist
#     b, a = butter(order, [low, high], btype='band')
#     return b, a

# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
#     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = filtfilt(b, a, data)
#     return y

# # Apply bandpass filter to FFT result
# fs = 1  # Assuming data is sampled at 1 Hz
# lowcut,highcut = st.slider("Select Low and High Cut Frequencies", min_value=0, max_value=fs/2, value=(0.1, round(len(t_day_fft)/2 - 1)), step=0.01)

# sr = st.slider('Sample Rate', min_value=200, max_value=20000, value=1000)

# low, high = st.slider(
#     'Select Low and High Cut Frequencies',
#     min_value=500, max_value=20000, value=(50, round(sr/2 - 1)), step=10)

# filtered_fft = butter_bandpass_filter(np.abs(t_day_fft), low, high, sr)

# # Plot filtered FFT
# plt.figure(figsize=(12, 6))
# plt.plot(frequencies[:len(frequencies)//2], filtered_fft[:len(frequencies)//2])
# plt.xlabel('Frequency')
# plt.ylabel('Amplitude')
# plt.title(f"Bandpass Filtered FFT of Total index of {selected_file} daily (Lowcut={low}, Highcut={high})")
# st.pyplot(plt)
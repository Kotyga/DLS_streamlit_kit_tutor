import streamlit as st
import datetime

# Button
st.button("Click here")

# Check box
selected = st.checkbox("Accept terms")

# Select box
option = st.selectbox(
     'Choose model mode:',
     ('CPU only', 'GPU'))
st.write('You selected:', option)

# Date input
day = st.date_input(
     "When is your birthday?",
     datetime.datetime.today())
st.write('Your birthday is:', day)

# Time input
time = st.time_input("Time")

# Multi select
selections = st.multiselect("Photo style:", ["Kuindzhi", "Kandinsky", "Malevich"])

# Number input
choice = st.number_input("Choose the number of epochs", 0, 50)

# Text area
text = st.text_area("Send feedback on the model's work")

# File upload
data = st.file_uploader("Share png file", type=['png'])

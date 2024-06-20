import streamlit as st
from datetime import time


# слайдер
st.slider(
    "label",
    min_value=5,
    max_value=25,
    value=20,
    step=None,
)

# интервальный слайдер
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(17, 45))
)

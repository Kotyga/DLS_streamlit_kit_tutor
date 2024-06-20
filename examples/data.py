import streamlit as st
import pandas as pd

# students and marks
students = ["Вася Пупкин", "Амелия Беделия", "Гарри Гончар", "Барон Мюнхаузен"]
marks = [82, 23, 56, 100]

df = pd.DataFrame()
df["Student Name"] = students
df["Marks"] = marks

# display dataframe
st.dataframe(df)

# static table
st.table(df)

# metrics
st.metric("KPI", 56, 3)

# json
st.json(df.to_dict())

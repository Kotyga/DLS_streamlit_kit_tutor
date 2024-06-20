import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


# Matplotlib
arr = np.random.poisson(5, 10000)
fig, ax = plt.subplots()
ax.hist(arr)
plt.grid()
st.pyplot(fig)

# Plotly
df = px.data.iris() #data
#create a fig object, define the data, x-axis, y-axis, 3rd dimension as color, title.
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
st.plotly_chart(fig, use_container_width=True)

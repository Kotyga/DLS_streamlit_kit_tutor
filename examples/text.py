import streamlit as st

# Title
st.title("Document Title")

# Header
st.header("Article header", anchor=None)

# Subheader
st.subheader("Article subheader")

# Text
st.text("This is a text!")

# Markdown
st.markdown('Streamlit is **_very_ cool**.')

# Code
st.code("y = mx + c")

# Code (specify language)
code = '''def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)'''
st.code(code, language='python')

# Latex
st.latex(r"\lim\limits_{x \to 0} \frac{\sin x}{x} = 1")

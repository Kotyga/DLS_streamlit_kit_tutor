import streamlit as st

# Show celebratory balloons
st.balloons()

# Show an error message
st.error("Error")

# Display a warning message
st.warning("Warning")

# Display informational messages
st.info("Info")

# Display success messages
st.success("Success")

# Display an exception in your application
exp = ValueError('ValueError')
st.exception(exp)

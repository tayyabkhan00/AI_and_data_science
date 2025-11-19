import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a chart:", ["Line", "Bar", "Area"])

# Create some random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.write(f"You selected: {option} chart")

if option == "Line":
    st.line_chart(data)
elif option == "Bar":
    st.bar_chart(data)
elif option == "Area":
    st.area_chart(data)

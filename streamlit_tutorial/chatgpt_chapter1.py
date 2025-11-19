import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello Streamlit!")
st.write("This is my first Streamlit app 🎉")

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is simple text")
st.markdown("**Bold text using Markdown**")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
agree = st.checkbox("I agree to terms")

if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")

df = pd.DataFrame({
    "Name": ["Aafi", "Tayyab", "Ali"],
    "Age": [10, 20, 25]
})

st.dataframe(df)  # interactive table
st.table(df)      # static table


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a view:", ["Home", "Data", "About"])



# Each option runs a different section
if option == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Home section!")

elif option == "Data":
    st.title("📊 Data Section")
    st.write("This is where your data or charts will appear.")

elif option == "About":
    st.title("ℹ️ About Section")
    st.write("This app is built with Streamlit.")

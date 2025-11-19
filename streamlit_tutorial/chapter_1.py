import streamlit as st

st.title("chai maker app")
if st.button("make chai"):
    st.success("chai is ready!")

add_masala = st.checkbox("add masala")
if add_masala:
    st.write("masala added")

tea_type = st.radio("choose tea type", ["green", "black", "herbal"])
st.write(f"You selected {tea_type} tea")
 
flavor = st.selectbox("choose flavor", ["ginger", "cardamom", "tulsi"])
st.write(f"You selected {flavor} flavor")

sugaer_level = st.slider("select sugar level", 0, 5, 2)
st.write(f"Sugar level: {sugaer_level}")

cups = st.number_input("number of cups", min_value=1, max_value=10, value=1)
st.write(f"Number of cups: {cups}")

st.date_input("select date")
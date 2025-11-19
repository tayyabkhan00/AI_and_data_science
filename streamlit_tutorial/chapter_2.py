import streamlit as st

st.title("Basic Streamlit App")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.image("https://i.pinimg.com/1200x/a8/fa/56/a8fa56068f96b6cb7a6456cab629164b.jpg",width=300)
    vote1= st.button("Vote for Option 1")
        
with col2:
    st.header("Column 2")
    st.image("https://i.pinimg.com/736x/68/64/80/6864802541fd5314d7ae7d6a5c26481c.jpg",width=300)
    vote2= st.button("Vote for Option 2")

if vote1:
    st.success("You voted for Option 1!")
elif vote2:
    st.success("You voted for Option 2!")

name= st.sidebar.text_input("Enter your name:")
options= st.sidebar.selectbox("Select your favorite option:", ["Option 1", "Option 2"])

with st.expander("See your input"):
    st.write(""" 1. Name
              2. Favorite Option
             3. Thank you for participating!""")

st.markdown('### welcome-message')
st.markdown('> Welcome to the Basic Streamlit App!')
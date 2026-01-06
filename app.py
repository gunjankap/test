import streamlit as st

st.set_page_config(page_title="My First App")

st.title("Streamlit Cloud App")
st.write("This Python runs on a real backend server.")

name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Hello {name} 👋")

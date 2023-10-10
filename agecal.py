import streamlit as st
st.title("First Jeida Software App")

name = st.text_input("Enter your name here")
yob = st.number_input("Enter your year of birth here",1900,2023,value=1950,step=1)
curr = st.number_input("Enter your current year here",2023,value=2023,step=1)
age = curr - yob

if st.button("Check My Age"):
    st.success(f"You are now {age} in year {curr}")
    st.text("hello")
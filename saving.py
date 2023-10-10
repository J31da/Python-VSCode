import streamlit as st
st.title("Weekly Savings App")

curr = st.text_input("Enter your currency")
sun = st.number_input("Enter Sunday's amount",10,value=100,step=1)
mon = st.number_input("Enter Monday's amount",15,value=100,step=1)
tue = st.number_input("Enter Tuesday's amount",20,value=100,step=1)
wed = st.number_input("Enter Wednesday's amount",25,value=100,step=1)
thu = st.number_input("Enter Thursday's amount",30,value=100,step=1)
fri = st.number_input("Enter Friday's amount",35,value=100,step=1)
sat = st.number_input("Enter Saturday's amount",40,value=100,step=1)
total = sun + mon + tue + wed + thu + fri + sat

if st.button("See my Savings for the Week"):
    st.success(f"Congratulation, you have saved {curr} {total} ")


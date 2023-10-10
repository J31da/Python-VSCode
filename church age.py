import streamlit as st
st.title("Church Age Checker")

name = st.text_input("What is your name? ")
age = st.number_input("How old are you? ",3,65,value=20,step=1)

if age < 13 and age >= 2:
  st.write(f"Welcome brother or sister {name} to the kids class. Make sure your parents have signed your form.")

elif age <= 19 and age >= 13:
  st.write(f"Welcome brother or sister {name} to the teens class. You will be sure to have a great time.")

elif age > 19:
  st.write(f"Welcome to the adult class {name}. Here, you will be learning advanced lessons.")

elif age < 2 and age > 0:
  st.write(f"Sorry to say {name}, but you are to young to attend.")



 
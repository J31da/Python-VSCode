import streamlit as st

if 'item' not in st.session_state:
    st.session_state.item = ""

item = st.text_input(f':blue' "What Item Would You Like?",key='item')

def addtolist():
    st.write(item)
if st.button("Add To List"):
    pass

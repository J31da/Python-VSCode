import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = ['Fashion','About Us']
choice = st.sidebar.selectbox('Menu',menu)

if choice == 'Fashion':
    st.subheader("Fashion")
    st.divider()

if choice == 'About Us':
    st.subheader("About Us")
    st.divider()
import streamlit as st
from PIL import Image

menu = st.sidebar.selectbox('Menu',['Upload File', 'About Us'])

if menu == "Upload File":
    st.subheader('Upload Your Files Here')

    image_file= st.file_uploader('Upload Your Image',type=['png','jpg','jpeg'])

    if image_file is not None:
         st.image(Image.open(image_file))


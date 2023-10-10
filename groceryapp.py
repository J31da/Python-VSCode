import streamlit as st
st.set_page_config(layout='wide')
bill = 0

st.subheader("Grocery Store")
st.divider()
st.image("https://health.clevelandclinic.org/wp-content/uploads/sites/3/2016/03/shoppingFruit-1257380437-770x553-1.jpg")

import streamlit as st

st.subheader("Meet our Team")
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Robert Anderson")
   st.divider()
   st.image("https://www.allprodad.com/wp-content/uploads/2021/03/05-12-21-happy-people.jpg")
with col2:
   st.subheader("Susan Hazlewood")
   st.divider()
   st.image("https://thetyee.ca/News/2023/04/23/NelWieman.jpg")

with col3:
   st.subheader("Andrea Smiths")
   st.divider()
   st.image("https://www.ohchr.org/sites/default/files/styles/hero_5_image_desktop/public/2023-04/Christine-Salloum---972x700.JPG?itok=n4mJf-xj")

st.header("")
st.subheader("Our Story")
st.divider()
st.subheader("Committed to providing quality organic food, this Grocery Store is one of the best supermarkets in Dubai where you can find a wide range of local and international products. From ice-cream to seafood to poultry and ready meals, we have pretty much everything in our store for customers. We have various branches in the city.")
st.divider()

st.header("")

st.subheader("Start Shopping")
st.divider()
option = st.selectbox(
    'What Fresh Fruits Would You Like Today?',
    ('Apple', 'Banana', 'Pear', 'Watermelon', 'Grapes', 'Mango', 'Kiwi', 'Cucumber'))

st.write('You selected:', option)

many = st.number_input("How many fruits do you wany",1,value=4,step=1)
bill = 3.4 * many

if st.button("See Bill"):
 st.success(f"The price is $ {bill} ")
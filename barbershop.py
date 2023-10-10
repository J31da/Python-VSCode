import streamlit as st
st.set_page_config(layout='wide')
bill = 0

st.subheader("Barber Shop")
st.divider()
st.image("https://www.chapsandco.com/ae/wp-content/uploads/sites/12/2022/07/chaps-and-co-bloomingdales-dubai-mall-1-1.png")

import streamlit as st

st.subheader("Demo Haircuts")
st.divider()
col1, col2, col3, col4= st.columns(4)

with col1:
   st.subheader("Buzz Cut")
   st.divider()
   st.image("https://www.menshairstyletrends.com/wp-content/uploads/2020/05/buzz-cut-low-fade-short-beard-los_the_barber-.jpg")
with col2:
   st.subheader("Mullet")
   st.divider()
   st.image("https://i0.wp.com/therighthairstyles.com/wp-content/uploads/2023/02/29-short-permed-hairstyle-with-temple-fade.jpg?resize=500%2C577&ssl=1")
with col3:
   st.subheader("Quiff")
   st.divider()
   st.image("https://content.latest-hairstyles.com/wp-content/uploads/barber-approved-1950s-quiff-style.jpg")
with col4:
   st.subheader("Crewcut")
   st.divider()
   st.image("https://content.latest-hairstyles.com/wp-content/uploads/buzz-cut-with-designs-for-men.jpg")


st.subheader("HairCuts for Males")
st.divider()
option = st.selectbox(
   'What Fresh Fruits Would You Like Today?',
   ('Crewcut', 'BuzzCut', 'BuzzCut w/ Fade', 'Mullet', 'Quiff', 'Pompadour', 'Layered', 'Bald', 'Shampooing'))

st.write('You selected:', option)

age = st.number_input("How old is the customer? ",step=1)
if age < 13 and age >= 2:
 age +=30
elif age <= 19 and age >= 13:
 age +=40
elif age > 19:
 age +=50
elif age < 2 and age > 0:
  st.error("Sorry, but the bustomer is too young.")


if st.button("See Bill"):
 st.success(f"The price is $ {age} ")
#https://docs.google.com/document/d/1UErecD2mH7_Cw4tmismgD-MkWFbzITidJkraODXQ6j4/edit?usp=sharing
import streamlit as st
st.set_page_config(layout='wide')
bill = 0
st.title("Papa Paul's Pizzeria")
st.image(" https://images.phi.content-cdn.io/yum-resources/e24b4731-a903-4b92-b9ab-b7bdeb0fee6d/Images/userimages/20-07-2023/uVC1G27sxnTvsad4vcjkvQ==/PH_SignaturePizza_WebsiteDealsBanner_UAE_EN-01.jpg")

st.subheader("Toppings")
st.subheader("Order 2 of the same Pizza to get 30% OFF!")
st.image("https://ygo-assets-websites-legacy.yougov.net/cumulus_uploads/entry/45715/pizza%20toppings%20AdobeStock_244985907.jpg?pw=1200")


st.subheader("Mushrooms")
mushroom1,mushroom2,mushroom3,mushroom4 = st.columns(4)


with mushroom1:
    if st.checkbox("Mushrooms: $30"):
        bill +=30
        st.success("Added to menu")

with mushroom2:
    if st.checkbox("Mushrooms & Olives; $30"):
        bill +=30
        st.success("Added to menu")

with mushroom3:
    if st.checkbox("Mushrooms & Cheese; $30"):
        bill +=30
        st.success("Added to menu")

with mushroom4:
    if st.checkbox("Mushrooms & Pineapple; $30"):
        bill +=30
        st.success("Added to menu")


st.subheader("Vegan")
vegan1,vegan2,vegan3,vegan4 = st.columns(4)


with vegan1:
    if st.checkbox("Normal; $40"):
        bill +=40
        st.success("Added to menu")

with vegan2:
    if st.checkbox("Olives; $40"):
        bill +=40
        st.success("Added to menu")

with vegan3:
    if st.checkbox("Mushroom; $40"):
        bill +=40
        st.success("Added to menu")

with vegan4:
    if st.checkbox("Pineapple; $40"):
        bill +=40
        st.success("Added to menu")


st.subheader("BBQ Sauce")
bbq1,bbq2,bbq3,bbq4 = st.columns(4)


with bbq1:
    if st.checkbox("Plain; $45"):
        bill +=45
        st.success("Added to menu")

with bbq2:
    if st.checkbox("Tomato Sauce; $45"):
        bill +=45
        st.success("Added to menu")

with bbq3:
    if st.checkbox("Mushrooms & Chicken; $45"):
        bill +=45
        st.success("Added to menu")

with bbq4:
    if st.checkbox("Chicken; $45"):
        bill +=45
        st.success("Added to menu")



st.subheader("Specials")
special1,special2,special3,special4 = st.columns(4)


with special1:
    if st.checkbox("Deepdish; $45"):
        bill +=55
        st.success("Added to menu")

with special2:
    if st.checkbox("Doubles; $45"):
        bill +=55
        st.success("Added to menu")

with special3:
    if st.checkbox("Hawaian; $45"):
        bill +=50
        st.success("Added to menu")

with special4:
    if st.checkbox("Custom; $45"):
        bill +=60
        st.success("Added to menu")

st.success(f"The price is $ {bill} ")

many = st.text_input("Will you be sharing your bill with others? ")
if many == "Yes" or "yes":
  many2 = st.number_input("How many people will you be sharing the bill with?",2,value=5,step=1)
  nwbill = bill / many2
  if st.button("See Bill"):
     st.success(f"The new price is $ {nwbill} for each person")
else:
    if st.button("See Bill"):
     st.success(f"The original price is $ {bill} ")

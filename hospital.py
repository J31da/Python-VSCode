import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Patient','Patient Database']
choice = st.sidebar.selectbox('Menu',menu)

if choice == 'Patient Database':
    df= pd.read_csv('hospitalpatients.csv')
    st.dataframe(df)



if choice == 'Register Patient':
 st.title(":orange[Hospital Patient Registration]") #colors: blue, green, orange, red, violet.
 title,dor = st.columns(2)

 with title:
     st.subheader(":orange[Patients Personal Details]") 
     titles = ["Mr", "Mrs", "Miss", "Ms"]
     title = st.radio('Select Title',titles,horizontal=True)

 with dor:
     st.header("")
     Dor = st.date_input("Date of Registration")

 fn,ln = st.columns(2)
 
 with fn:
     name = st.text_input("First Name: ")

 with ln:
    lastname = st.text_input("Last Name: ")
       
 dob,gender = st.columns(2)

 with dob:
     Dob = st.date_input("Date of Birth")

 with gender:
     Gender = ["Male", "Female"]
     chosengender = st.radio('Select Gender',Gender,horizontal=True)

 st.divider()

 st.subheader(":orange[Patient's Contact Details]")
 
 num,address = st.columns(2)

 with num:
     mobilenum = st.text_input("Mobile Number")

 with address:
     Address = st.text_input("Address")
 
 homenum,mail = st.columns(2)

 with homenum:
     homenum = st.text_input("Home Number")

 with mail:
     Mail = st.text_input("Mail")

 home,postcode = st.columns(2)
 
 with home:
     country = st.text_input("City/Town")

 with postcode:
     Postcode = st.text_input("Postcode")


 df= pd.read_csv('hospitalpatients.csv')
 def add_patients(title,Dor,name,lastname,Dob,chosengender,mobilenum,Address,homenum,Mail,country,Postcode,df):
  patients_dict = {'Title':title,'Date Of Registration':Dor,'First Name':name,'Last Name':lastname,'Date Of Birth':Dob,'Gender':chosengender,
                   'Mobile Number':mobilenum,'Address':Address,'Home Number':homenum,'Mail':Mail,'Location':country,'Postcode':Postcode}
  patients_df = pd.DataFrame([patients_dict]) 
  df = pd.concat([df,patients_df],ignore_index=True) 
  return df

 if st.button("Register"):
     df = add_patients(title,Dor,name,lastname,Dob,chosengender,mobilenum,Address,homenum,Mail,country,Postcode,df)
     df.to_csv('hospitalpatients.csv',index=False)

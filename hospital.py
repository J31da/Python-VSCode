import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Patient','Patient Database','Find Patient']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('hospitalpatients.csv')
patient_id = 'PATIENT' + str(len(df) + 1)

if choice == 'Patient Database':
    st.dataframe(df,use_container_width=True)

    



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

 df = pd.read_csv('hospitalpatients.csv')

 if st.button("Register"):
     if (patient_id and title and Dor and name and lastname and Dob and chosengender and mobilenum and Address and homenum and Mail and country and Postcode):
        patient_df = pd.DataFrame({'Patient ID':[patient_id],'Title':[title],'Date Of Registration':[Dor],'First Name':[name],'Last Name':[lastname],'Date Of Birth':[Dob],'Gender':[chosengender],
                   'Mobile Number':[mobilenum],'Address':[Address],'Home Number':[homenum],'Mail':[Mail],'Location':[country],'PostCode':[Postcode]}) 
        new_df = pd.concat([df,patient_df],ignore_index=True)
        new_df.to_csv('hospitalpatients.csv',index=False)
        st.success("Successfuly Registered!")

     else:
         st.error("Kindly Fill In All Boxes")

 
if choice == 'Find Patient':
    spc1,spc2,fspc = st.columns([2,1,1.7])
    with fspc:
        st.subheader("Find Patient Details")
        st.write("")
        fn1,fn2 = st.columns([2,1])
        with fn1:
            find = st.text_input("Enter Patient ID")
            st.write("")
            fnbut = st.button("Find Patient")

    if fnbut:
        if find:
            fnd_result = df[df['Patient ID'] == find]
            getttle = fnd_result['Title'].iloc[0]
            getdor = fnd_result['Date Of Registration'].iloc[0]
            getfn = fnd_result['First Name'].iloc[0]
            getln = fnd_result['Last Name'].iloc[0]
            getdob = fnd_result['Date Of Birth'].iloc[0]
            getgen = fnd_result['Gender'].iloc[0]
            getmobnum = fnd_result['Mobile Number'].iloc[0]
            getadd = fnd_result['Address'].iloc[0]
            gethomenum = fnd_result['Home Number'].iloc[0]
            getmail = fnd_result['Mail'].iloc[0]
            getloc = fnd_result['Location'].iloc[0]
            getpostc = fnd_result['PostCode'].iloc[0]

            st.write("")
            sp1,sp2,sp3 = st.columns([0.5,2,0.5])
            with sp2:
                space = " "

                fulln = getttle + space + getfn + space + getln
                st.subheader(f':blue[{fulln}]')
                st.divider()
                

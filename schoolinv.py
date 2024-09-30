'''
schoolfees invoice (multipage menu)
first page (REGISTER STUDENT)
-ask to register student
name, class, parentname, email, phone, address
---

second page (ADD PAYMENT)
-then add schoolfees payment section,
search studentID (show student name and class) using PANDAS
then choose year and session/term like '2024 first term' in dropdown
and enter fees made with date input (students can make multiple payments in each session,(idea:list to add ))
---

third page (DOWNLOAD RECIEPTS)
search studentID (show name and year of student to confirm search) using PANDAS
-filter per year and per session/term  '2024 first term' etc 
download the payment invoice above using FPDF
---

forth page (ADMIN ROLES)
delete student or payment using PANDAS
add new year session (for teachers to include new year/session/terms)
'''

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Menu',['Enrollment', 'Tuition Fees', 'Download Receipt', 'Admin Roles'])

admission = pd.read_csv('schoolinv.csv')
country = pd.read_csv('countries.csv')
country_list = country['Country'].to_list()

studid = 'Student'+str(len(admission)+1)


if menu == 'Enrollment':
    st1,st2,st3 = st.columns([0.2,4,0.2])

    with st2:
        with st.form('Create Admission Form',clear_on_submit=True):
            st.header('**:blue[Student Admission]**')
            st.divider()
            
            st.write('')

            nm1,nm2,nm3 = st.columns(3)

            with nm1:
                fn = st.text_input("Child's First Name")
            with nm2:
                mn = st.text_input("Child's Middle Name (optional)")
            with nm3:
                ln = st.text_input("Child's Last Name")

            st1,st2 = st.columns(2)

            with st1:
                na = st.selectbox("Nationality", country_list)

            with st2:
                gr = st.selectbox(
            'Class',
            ('Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'))

            st.write('')

            st.divider()
            st.header('**:blue[Parent Information]**')
            st.write('')


            pn1,pn2 = st.columns(2)

            with pn1:
                pfn = st.text_input("Parent/Guardian's First Name")
            with pn2:
                pln = st.text_input("Parent/Guardian's Last Name")

            em1,ph2 = st.columns(2)

            with em1:
                em = st.text_input("Email Adress")
            with ph2:
                phn = st.text_input("Phone Number")

            address = st.text_input('Address')

            st.write('')

            bt1,bt2 = st.columns(2)

            with bt1:
               if st.form_submit_button('Apply'):
                if fn and ln and na and pfn and pln and em and phn and address:
                   scdict = {'StudentID':[studid],"Student's First Name":[fn],"Student's Middle Name":[mn],"Student's Last Name":[ln],"Nationality":[na],"Grade":[gr],
                             "Parent/Guardian's First Name":[pfn],"Parent/Guardian's Last Name":[pln],"Email Address":[em],"Phone Number":[phn],
                             "Address":[address]}
                   sc_df = pd.DataFrame(scdict)
                   scjoin = pd.concat([admission,sc_df],ignore_index=True)
                   scjoin.to_csv('schoolinv.csv',index=False)

                   st.success('Successfully Filled!')
                else:
                   st.error('Complete Required Fields')

if menu == 'Tuition Fees':
   
    with st.expander('View Admission Database'):
        st.table(admission)

    st.subheader('')

    find1,find2 = st.columns([0.4,1])
    with find1:
        findID = st.text_input(':blue[Enter Student ID]')
        findbut = st.button('Find')

    if findbut:
        if findID:
            searchresult = admission[admission['StudentID'].str.lower() == findID.lower()]
            #st.write(searchresult)

            getfn = searchresult["Student's First Name"].iloc[0]
            getmn = searchresult["Student's Middle Name"].iloc[0]
            getln = searchresult["Student's Last Name"].iloc[0]
            getgr = searchresult["Grade"].iloc[0]

            st.subheader(f':blue[{getfn}  {getln}]')
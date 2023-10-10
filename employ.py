import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Staff','Staff Database','Staff File']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('employee.csv')
user_id = 'USER' + str(len(df) + 1)

if choice == 'Staff Database':
    st.dataframe(df,use_container_width=True)



if choice == 'Register Staff':
 st.subheader("Employee's Name")
 fn,ln = st.columns(2)
 with fn:
     name = st.text_input("First Name: ")
 with ln:
     name2 = st.text_input("Last Name: ")
 mail,gender = st.columns(2)
 with mail:
     mail = st.text_input("Email Adress: ")
 with gender:
     gender = st.selectbox(
         'Gender',
         ('Male', 'Female', 'Other'))
     
 department = st.selectbox(
    'Department',
    ('Management', 'Accounting', 'Engineering', 'Human Resources', 'Security', 'Medical', 'Transportation')) 

 jobttle = st.selectbox(
    'Job Title',
    ('Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'))
 
 tmspent,salary = st.columns(2)
 with tmspent:
     timespent = st.selectbox(
         'Contract Status',
         ('Full Time', 'Part Time'))
 with salary:
     salary = st.number_input("Monthly Income: ",0,value=10000,step=100)

 edulevel = st.selectbox(
     'Educational Degree',
     ('None', 'Associate Degree', 'Bachelor Degree', 'Graduate Degree', 'Professional Degree', 'Doctoral Degree'))
 
 date = st.date_input("Employememt Date")
 
 df= pd.read_csv('employee.csv')
 def add_employ(user_id,name,name2,date,salary,gender,mail,department,jobttle,edulevel,timespent,df):
  employ_dict = {'User ID':user_id,'First Name':name,'Last Name':name2,'Date of Employment':date,'Salary':salary,'Gender':gender,'Mail Address':mail,'Department':department,
                  'Seniority Level':jobttle,'Education Level':edulevel,'Contract Status':timespent}
  employ_df = pd.DataFrame([employ_dict]) 
  df = pd.concat([df,employ_df],ignore_index=True) 
  return df

 if st.button("Submit Employee Survey"):
     if (user_id and name and name2 and date and salary and gender and mail and department and jobttle and edulevel and timespent):
            df = add_employ(user_id,name,name2,date,salary,gender,mail,department,jobttle,edulevel,timespent,df)
            df.to_csv('employee.csv',index=False)
            st.success('Employee Data Saved')
     else :
         st.error('Kindly Fill All The Boxes')

if choice == 'Staff File':
   st.subheader("Find Employee Details")
   space1,space2,finder = st.columns([2,2,1.5])
   with finder:
        find = st.text_input("Enter Employee ID ")
        if st.button("Find Employee"):
            if find:
                find_result = df[df['User ID'] == find ]
                getfn = find_result['First Name'].iloc[0]
                getln = find_result['Last Name'].iloc[0]
                getmail = find_result['Mail Address'].iloc[0]
                getgender = find_result['Gender'].iloc[0]
                st.subheader(getfn)
                st.write(f"Email: {getmail}")
                st.write(f"Gender: {getgender}")
                st.write(getln)


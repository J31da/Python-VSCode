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

try:
    admission = pd.read_csv('schoolinv.csv')
except:
    admission = pd.DataFrame()

country = pd.read_csv('countries.csv')

try:
    readsess = pd.read_csv('schoolsess.csv')
except:
    readsess = pd.DataFrame()

try:    
    readpay = pd.read_csv('schoolpay.csv')
except pd.errors.EmptyDataError:
    readpay = pd.DataFrame()


country_list = country['Country'].to_list()
studid = 'Student'+str(len(admission)+1)
#-----------------------------------------------

if 'find_button' not in st.session_state:
    st.session_state.find_button = False

#-----------------------------------------------
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

            #-------------------------------- upload & save image
            img1, img2 = st.columns([0.7,0.3])

            with img1:
                upimg = st.file_uploader("Upload Child's Photo",type = ['jpg', 'jpeg', 'png'])
                if upimg:
                    imgname = f'{studid}.png'
                    with open (imgname, 'wb') as writeimg:
                        writeimg.write(upimg.getbuffer())

            
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
                if fn and ln and na and pfn and pln and em and phn and address and upimg:
                   scdict = {'StudentID':[studid],"Student's First Name":[fn],"Student's Middle Name":[mn],"Student's Last Name":[ln],"Nationality":[na],"Grade":[gr],
                             "Parent/Guardian's First Name":[pfn],"Parent/Guardian's Last Name":[pln],"Email Address":[em],"Phone Number":[phn],
                             "Address":[address]}
                   sc_df = pd.DataFrame(scdict)
                   scjoin = pd.concat([admission,sc_df],ignore_index=True)
                   scjoin.to_csv('schoolinv.csv',index=False)

                   st.success('Successfully Filled!')
                else:
                   st.error('Complete Required Fields')

#-----------------------------------------------
if menu == 'Tuition Fees':
   
    with st.expander('View Admission Database'):
        st.table(admission)


    find1,find2,find3 = st.columns([0.4,0.4,0.6])
    with find1:
        st.subheader('')

        findID = st.text_input(':blue[Enter Student ID]')
        findbut = st.button('Find')


    st.subheader('')

    if findbut:
        st.session_state.find_button = True
        
    if st.session_state.find_button == True:
        if findID:
            try:
                searchresult = admission[admission['StudentID'].str.lower() == findID.lower()]
                st.write('')

                #st.write(searchresult)

                getfn = searchresult["Student's First Name"].iloc[0]
                getmn = searchresult["Student's Middle Name"].iloc[0]
                getln = searchresult["Student's Last Name"].iloc[0]
                getgr = searchresult["Grade"].iloc[0]
                getid = searchresult["StudentID"].iloc[0]

                getgsf = readsess[readsess['Grade'] == getgr]
                getsf = getgsf['School Fees'].iloc[0]

                st.sidebar.divider()
                payactivate = st.sidebar.toggle(f'Update {getfn} Payment')
                

                with find1:

                    st.divider()
                    st.image(f'{getid}.png',width=200)

                with find3:
                    st.subheader('')

                    st.subheader(f':blue[{getfn}  {getln}]')
                    st.write(f'**{getgr}**')
                    st.divider()

                    allsess = getgsf['School Sessions']
                    #allsess = readsess['School Sessions']
                    choosesess = st.selectbox('**Choose Session To Make Payment**',allsess)
                    st.write('')

                    choosedate = st.date_input('**Choose Date Of Payment**')
                    st.write('')

                    filterpay = readpay [(readpay['Name'] == f'{getfn} {getln}') & (readpay['Grade'] == getgr) & (readpay['School Sessions'] == choosesess) & (readpay['School Fees'] > 0)]
                    #st.table(filterpay)
                    
                    
                    if filterpay.empty:
                        pay = False
                        st.write(f'**:blue[{getgr} Payment]**')
                        st.error(f'${getsf:,}')
                    else:
                        st.write(f'**:blue[{getgr} Payment]**')
                        st.info(f'${getsf:,}')

                    
                    
                    if payactivate:
                        paybutt = st.sidebar.pills(f"**{getfn}  {getln}'s :blue[Payment]:**",['Delete Payment','Payment Made'])
                        

                        if paybutt == 'Payment Made':
                            st.sidebar.divider()
                            st.sidebar.write('')
                            paycof = st.sidebar.radio('**Confirm :blue[Payment]:**',['Unpaid', 'Paid'],horizontal=True)
                            st.sidebar.divider()
                            
                            if paycof == 'Paid':
                                st.sidebar.write('')

                                paydict = {'Name':[f'{getfn} {getln}'],'School Sessions':[choosesess],'Grade':[getgr],'School Fees':[getsf],'Date of Payment':[choosedate]}
                                paytable = pd.DataFrame(paydict)
                                payjoin = pd.concat([readpay,paytable],ignore_index=True)
                                payjoin.to_csv('schoolpay.csv',index=False)

                            else:
                                pass
                        
                        if paybutt == 'Delete Payment':
                                
                            st.sidebar.write('')
                            st.sidebar.divider()
                            st.sidebar.info('Adjustments Require Admin Role')
                            st.sidebar.divider()
                           
                    else:
                        pass

                        
                    #paysess = st.number_input('**Enter Payment Amount**',0,step=10000)

                    st.write('')
            except IndexError:
                inv1,inv2 = st.columns([0.35,0.7])
                with inv1:
                    st.error('Invalid Student ID')
        


#-----------------------------------------------
if menu == 'Admin Roles':

    st.sidebar.write('')
    adpass,adpass2 = st.sidebar.columns(2)

    with adpass:
        adminpass = st.sidebar.text_input('**Enter Admin Password**',type='password')
    
    if adminpass == '1234':
        sp1, sp2 = st.columns([0.6,0.4])

        with sp1:
            readsess = pd.read_csv('schoolsess.csv')
            with st.expander('View All Sessions'):
                st.table(readsess)
            try:
                lastsess = readsess['School Sessions'].iloc[-1]
        
                st.divider()
                st.subheader(f'Last School Session: ')
                st.subheader(f' :blue[{lastsess}]')
                st.divider()
            except:
                st.info('Sorry, No Data to Show Yet')
        cl1,cl2,cl3,cl4 = st.columns([0.35,0.3,0.3,0.2])

        with cl2:
            st.subheader('')  
            addgrade = st.selectbox(
        '**Choose :blue[Grade]**',
        ('Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'))
            st.write('')    

            with cl3:
                st.subheader('')  
                addfee = st.number_input(f'**Enter :blue[|{addgrade}|] Fees**',0,step=10000)
                st.write('')    

            with cl1:
                st.subheader('')
                addsess = st.text_input('**Enter Session: :blue[(e.g 24|25 First Term)]**')
        
                st.write('')
                if st.button('Add New Session'):
                    sessdict = {'School Sessions':[addsess],'School Fees':[addfee],'Grade':[addgrade]}
                    sesstable = pd.DataFrame(sessdict)
                    sessjoin = pd.concat([readsess,sesstable],ignore_index=True)
                    sessjoin.to_csv('schoolsess.csv',index=False)
                    st.success(f'{addsess} Added')
            
        st.write('')
        st.divider()

        st.subheader('Delete :blue[Student Data]')
        st.write('')

        editstu = st.data_editor(readpay,use_container_width=True)
        if st.toggle('**Save :blue[Changes]**'):
            if st.button('Confirm'):
                editstu.to_csv('schoolpay.csv')
                st.info('Edits Saved')

            
        
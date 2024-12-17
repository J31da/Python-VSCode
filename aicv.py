import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title='AI CV Generator',page_icon='📄')

st.sidebar.title('**AI CV Generator**')
st.sidebar.divider()

m_api_key = "AIzaSyBcMUmbR0O8jKUv-yR0mQhAGvdyekAeu5M"

#AI Config Settings
def config_ai():
    genai.configure(api_key=m_api_key)
    return genai.GenerativeModel('gemini-pro')

#Start-Up Gemini AI
model = config_ai()

#AI CV Template
def details_prompt(name,address,email,contact,keyskills,workexp,edu):
    
    global cont_response,prof_response,kysk_response,workxp_response,edu_response

    prof_prompt = f"""
    Extract the information below and use it to design a professional summary for my cv. Make it 4-5 lines. Do not include the header. No format, no asterisk

    My key skills  {keyskills}

    My work experience {workexp}

    My education {edu}
    """

    key_skills = f"""
    Also extract the information below and use it to design my key skills,in bullet points, for my professional cv. Do not include the header. No format, no asterisk

    My key skills  {keyskills}

    """

    workxp_prompt = f"""
    Also extract the information below and use it to design a comprehensive, brief work experience for my professional cv, , use information available to design a 3-4 line description of each work experience mentioned. include timeline. Do not include the header. No format, no asterisk. 

    My work experience {workexp}

    """

    edu_prompt = f"""
    Also extract the information below and use it to design my educational background for my professional cv. Do not include the header. No format, no asterisk. space between each line
    
    My education {edu}

    """

    
    try:
        prof_content = model.generate_content(prof_prompt)
        prof_response = prof_content.text

        st.info('Professional Summary')
        st.text_area('',value=prof_response,height=160)
        st.divider()

        kysk_content = model.generate_content(key_skills)
        kysk_response = kysk_content.text

        st.info('Key Skills')
        st.text_area('',value=kysk_response,height=150)
        st.divider()

        workxp_content = model.generate_content(workxp_prompt)
        workxp_response = workxp_content.text

        st.info('Work Experience')
        st.text_area('',value=workxp_response,height=450)
        st.divider()

        edu_content = model.generate_content(edu_prompt)
        edu_response = edu_content.text

        st.info('Educational Background')
        st.text_area('',value=edu_response,height=150)
        st.divider()
    except:
        st.error('Error Composing CV')
        return None


st.sidebar.info('Provide your detailed response to generate a good resume.')

name = st.sidebar.text_input('Enter Your Full Name',placeholder='Eva Smith')
address = st.sidebar.text_input('Enter Address',placeholder='19 Wuthering Heights St.')

if st.sidebar.checkbox('Add Email'):
    email = st.sidebar.text_input('e',placeholder='evasmith@gmail.com',label_visibility='collapsed')
else:
    email = ''

if st.sidebar.checkbox('Add Contact'):
    contact = st.sidebar.text_input('c',placeholder='+212-456-7890',label_visibility='collapsed')
else:
    contact = ''

st.sidebar.subheader('')
keyskills = st.sidebar.text_area('**Key Skills [One Per Line]**',height=150,
placeholder='''Art Direction and Photography

Video Production and Editing

UX/UI Design Principles''')

workexp = st.sidebar.text_area('**Work Exprience With Dates [One Per Line]**',height=150,
placeholder='''UX Designer at Microsoft: [2000-2006]

Freelance Director: [2006-2010]

Social Media Manager: [2010-2015]''')

edu = st.sidebar.text_area('**Education With Dates [One Per Line]**',height=210,
placeholder='''Fine Arts, Stanford University:  [1980-1984]

Liberal Arts, Harvard University: [2016-2020]

Philosophy, Yale University:         [2021-2024]''')

if st.sidebar.button('Generate CV'):
    if name and address and keyskills and workexp and edu:
        with st.spinner('Generating CV...'):
            generate_cv = details_prompt(name,address,email,contact,keyskills,workexp,edu)

        if generate_cv:
            st.sidebar.success('Your CV Has Been Successfully Generated!')
            
            
            
            
            

    else:
        st.sidebar.info('Fill In All Boxes')
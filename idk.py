#Enable users to upload and view a CSV file
#Enable users to upload and view an image file
#Enable users to upload and play an audio file
#Enable users to upload and play an video file


import streamlit as st
import pandas as pd
import plotly.express as px


menu = st.sidebar.selectbox("Choose an option",['Upload CSV','Upload Image','Upload Audio','Upload Video'])


if menu == 'Upload CSV':
    st.subheader("Upload CSV & View Database")
    uploadcsv = st.file_uploader("Upload your CSV file here",type='csv')


    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)


        with st.expander('View CSV Table'): #like a toggle (open and close)
            st.table(readcsv)
           
        readcsvcolumns = readcsv.columns #read all columns in csv file
       
        selectcolumns = st.multiselect('Choose Columns to plot',readcsvcolumns)
        col1,col2 = st.columns(2)
        with col1:
            selectoperator = st.radio("Choose Columns Stats Operator",['Average','Sum','Count'],horizontal=True)
        with col2:
            selectchart = st.radio("Choose Chart to plot",['Bar Chart','Pie Chart'],horizontal=True)


        if selectcolumns:
            if selectoperator == 'Average':
                ave_op = readcsv[selectcolumns].mean().reset_index()
                # st.table(ave_op)
                if selectchart == 'Bar Chart':
                    barchart = px.bar(ave_op, x= 'index', y=0,labels={'index':'Subject','0':'Average'})
                    st.plotly_chart(barchart)
                   
                elif selectchart == 'Pie Chart':
                    piechart = px.pie(ave_op, names= 'index', values=0,labels={'index':'Subject','0':'Average'})
                    st.plotly_chart(piechart)
                   
                    #.sum(), values, publish your work on streamlit share
               
               
       


#classwork: try the upload image page yourself
#hint of image formats/type: jpg, jpeg, png, webp
#skip: allow users to upload multiple files


if menu == 'Upload Audio':
    st.subheader("Upload Audio To Play")
    uploadaudio = st.file_uploader('Upload your audio file here',type=['mp3','wav'])
    if uploadaudio:
        st.audio(uploadaudio,format='audio/mp3')




if menu == 'Upload Video':
    st.subheader('Upload Youtube Video Link To Play')
    youtubelink = st.text_input("Paste In Your Youtube Video Link")


    if st.button("Play Youtube Video"):
        try:
            if youtubelink:
                st.video(youtubelink)
           


        except:
            st.error("Sorry cannot play this video link")


        #classwork:
        # put a button to click to play
        # check to handle errors


#ability test on uploadCSV
# use a multiselect to choose columns to plot: create a variable called columnslist = 'read your pandas file'.to_list()
# use a radio to choose statistical operators (sum,average,count) #check your previous work
# choose chart to display


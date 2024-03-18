import streamlit as st
import pandas as pd
import plotly.express as px

#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file

#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

st.set_page_config(layout='wide')
st.title('Student Scores Database')
#Open a csv file

choice = st.sidebar.selectbox('Menu',['Scores Database', 'Submit Scores'])
df = pd.read_csv('scores.csv')

if choice == 'Scores Database':
 st.table(df)

 sub = ['Maths','English','Science','History','Geography']
 sub_score = df[sub].mean().reset_index()
 sub_new = sub_score.rename(columns={'index':'Subjects', 0:'Average'})

 barchart = px.bar(sub_new, x = 'Subjects', y ='Average')
 st.plotly_chart(barchart)

 #grade_count = df['Grade'].count()


if choice == 'Submit Scores':
 st.divider()

 Name,Math = st.columns(2)
 with Name:
   name = st.text_input("Enter the student's name: ")
 with Math:
   maths = st.number_input("Enter the student's score for Maths: ",0,value=70,step=1)


 English,Science = st.columns(2)
 with English:
   english = st.number_input("Enter the student's score for English: ",0,value=70,step=1)
 with Science:
   science = st.number_input("Enter the student's score for Science: ",0,value=70,step=1)

 History,Geography = st.columns(2)

 with History:
   history = st.number_input("Enter the student's score for History: ",0,value=70,step=1)
 with Geography:
   geography = st.number_input("Enter the student's score for Geography: ",0,value=70,step=1)
 total = maths + english + science + history + geography
 average = total / 5

 if average < 40:
   grade = "F"

 elif average >= 40 and average < 50:
   grade = "E"

 elif average >= 50 and average < 60:
   grade = "D"
  
 elif average >= 60 and average <= 69:
   grade = "C"

 elif average >= 70 and average < 80:
   grade = "B-"

 elif average >= 80 and average < 90:
   grade = "B"

 elif average >= 90 and average < 95:
   grade = "A" 

 elif average >= 95 and average <= 100:
   grade = "A+"


# def add_student(name,maths,english,science,history,geography,total,average,grade,df):
#   student_dict = {'Name':name,'Maths':maths,'English':english,'Science':science,
#                   'History':history,'Geography':geography,'Total':total,'Average':average,'Grade':grade}
#   student_df = pd.DataFrame([student_dict]) #convert student dict into a df with columns and data
#   df = pd.concat([df,student_df],ignore_index=True) #append, concatenate the new student df to the existiing df
#   return df


 if st.button("Submit Student Scores"):
     
      students_dict = {'Name':[name],'Maths':[maths],'English':[english],'Science':[science],
         'History':[history],'Geography':[geography],'Total':[total],'Average':[average],'Grade':[grade]}
     
      students_df = pd.DataFrame(students_dict)
      new_df = pd.concat([df,students_df],ignore_index=True)
      new_df.to_csv('scores.csv',index=False)
      st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}")

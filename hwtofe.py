#Homework 1:
#Read any csv file and display as a dataframe




#Project Objective
# Create a student scores database which can
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F) using the average
# -save and update your csv file


#import streamlit as st
#import pandas as pd #used to read a csv file and convert to a table (dataframe)


#What is a CSV file?
#A CSV file is a text file that each data is separated by a comma (comma separated values)


#df = pd.read_csv('scores.csv')
#st.dataframe(df)


#co-teacher Jeida will teach us the following:
# set the page to be full width X
# the dataframe on full width X
# add total, avearge and grade to also appear on CSV file X
# collect students data, save as dictionary and convert to a dataframe X
# overwrite the CSV file and display it X
#In the end of the class, student should be able to add the name and the scores and it all appears in the CSV file


import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
df = pd.read_csv('homework.csv')


st.dataframe(df,use_container_width=True)




name = st.text_input("Pls enter your name")


math = st.number_input("How much did you get in Math",value=0)
english = st.number_input("How much did you get in english",value=0)
science = st.number_input("How much did you get in Science",value=0)
total = math + english + science


average = total / 3


if average >=0 and average <=85:
     grade = "F"
elif average >=35 and average <=86:
     grade = "D"
elif average >=55 and average <=87:
     grade = "C"
elif average >=65 and average <=88:
     grade = "B"
elif average >=80 and average <=89:
     grade = "A"
elif average >= 90:
     grade = "A+"
       


def add_student(name,math,science,average,total,grade,df):
    student_dict = {'Name':name, 'Math':math, 'Science':science,'English':english, 'Average':average, 'Total':total, 'Grade':grade}
    student_df = pd.DataFrame([student_dict])
    pd.concat([df,student_df],ignore_index=True)
    return df


if st.button("Submit Student Scores"):
    df = add_student(name,math,science,average,total,grade,df)
    df.to_csv('homework.csv',index=False)
    st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}.")

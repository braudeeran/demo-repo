import streamlit as st
import time
import pandas as pd
import os
import json
from MyList import my_list


st.markdown("<h1 style = 'text-align:center;'>This is my form</h1>", unsafe_allow_html=True )

if "my_li" not in st.session_state:
    st.session_state.my_li = []


# def doSomething():

#     myDict = {
#     "name" : st.session_state.fName,
#     "Last_name" : st.session_state.lName,
#     "E-mail" : st.session_state.mail,
#     "Password" : st.session_state.password,
#     "Date of birth" : f'{st.session_state.d_birth}-{st.session_state.m_birth}-{st.session_state.y_birth}'}

#     my_list.append(myDict)

#     df = pd.DataFrame.from_dict(my_list)

#     st.dataframe(df)




with st.form("myForm", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("What is your first name?", placeholder = "Name", key = "fName")
    l_name = col2.text_input("What is your last name?", key = "lName")
    mail = st.text_input("Email", key = "mail")
    password = st.text_input("password", type = "password", key = "password")
    st.text_input("confirm password", type = "password")
    day, month, year = st.columns(3)
    d_birth = day.text_input("day", key = "d_birth")
    m_birth = month.text_input("month", key = "m_birth")
    y_birth = year.text_input("year", key = "y_birth")
    status = st.form_submit_button("submit")

def makeDict(f_name, l_name, mail, password, d_birth, m_birth, y_birth):
    myDict = {
    "name" : f_name,
    "Last_name" : l_name,
    "E-mail" : mail,
    "Password" : password,
    "Date of birth" : f'{d_birth}-{m_birth}-{y_birth}'}
    return myDict

place = st.empty()
if status:

    myDict = makeDict(f_name, l_name, mail, password, d_birth, m_birth, y_birth)
    st.session_state.my_li.append(myDict)
    place.write(st.session_state.my_li)


# if status:
#     st.success("Submited!")
        
#     myDict = {
#     "name" : f_name,
#     "Last_name" : l_name,
#     "E-mail" : mail,
#     "Password" : password,
#     "Date of birth" : f'{d_birth}-{m_birth}-{y_birth}'}

#     my_list.append(myDict)

#     df = pd.DataFrame.from_dict(my_list)

#     st.dataframe(df)
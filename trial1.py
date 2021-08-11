# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:33:36 2021

@author: Divya Somakumar
"""

import streamlit as st
st.title("Parkinson's Detection App")
st.image("parkinsons.jpg",width=350)
st.text("This app tries to detect Parkinson's by examining the voice of the user")
Name=st.text_input("Name")
Age=st.text_input("Age")
Gender=st.selectbox("Gender", options=["Male","Female","Transgender"])
Weight=st.slider("Weight",min_value=0,max_value=100)
Record=st.button("Record")
st.text("Say Hello How are you?")

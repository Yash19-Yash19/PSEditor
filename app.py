



# importing libraries
import streamlit as st #web app and camera
import numpy as np # for image processing 
from PIL import Image #Image processing 
import cv2 #computer vision 
import os
import time


# Use wide option to view full page
st.set_page_config(layout="wide")


# setting up app title 
st.markdown(""" 
# PEditor
""")


# setting up menu  buttons
rad =st.sidebar.radio(" Menu",["Home","Help","About us","Contact us"])


# if else staements for switching from one option to another
if rad=="Home":

    # displaying an image and tagline
    st.markdown("""
    ##  PencilSketch Editor....
    #  Image  to Pencil Sketch 



    Before you convert  you have to upload or capture an image
    for the conversion of image to a pensil sketch image......😊🙂🙂😊😊
    """)


# adding ballons animation
    st.balloons()


    # connecting download features to sidebar functions
    with st.sidebar:
            st.title("PDF to Text")
            textOutput = st.selectbox(
                "How do you want your output data?",
                ('Capture Image', 'Upload Image'))
                
                              

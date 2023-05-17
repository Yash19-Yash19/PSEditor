import streamlit as st
from PIL import Image

icon = Image.open("sketchbook.png")
st.sidebar.image(icon, use_column_width=True,)

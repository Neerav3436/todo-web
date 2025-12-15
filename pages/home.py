import streamlit as sl
from PIL import Image 
#Pillow already part of streamlit

sl.title("This is Home Page")

camera_image = None
with sl.expander("Click to open camera"):
    camera_image = sl.camera_input("Take a picture", key="camera")

sl.write(sl.session_state)

if(camera_image is not None):
    img = Image.open(camera_image)

    gray_scale = img.convert("L")

    sl.image(gray_scale)
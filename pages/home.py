import streamlit as sl
from PIL import Image 
#Pillow already part of streamlit

sl.title("This is Home Page")

camera_image = None
with sl.expander("Click to open camera"):
    camera_image = sl.camera_input("Take a picture", key="camera")

uploaded_image = None
with sl.expander("Upload picture"):
    uploaded_image = sl.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="picture")

sl.write(sl.session_state)

if(camera_image is not None):
    img = Image.open(camera_image)

    gray_scale = img.convert("L")

    sl.image(gray_scale)

if(uploaded_image is not None):
    img = Image.open(uploaded_image)

    gray_scale = img.convert("L")

    sl.image(gray_scale)
import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

# 画像
image = Image.open('./data/補正前(海上試験Wit).png')
st.image(image, width=200)

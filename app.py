import streamlit as st
from PIL import Image

from extract_text import ExtractText


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """
            You are an expert in understanding invoices.
            You will receive input images as invoices &
            you will have to answer questions based on the input image
            """


if submit:

    get_text_obj = ExtractText()
    image_data = get_text_obj.preprocess(uploaded_file)
    response = get_text_obj.get_text(input_prompt,image_data,input)

    st.subheader("The Response is")
    st.write(response)


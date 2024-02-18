import os
import logging
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai


class ExtractText:
    def __init__(self) -> None:
        
        load_dotenv()
        genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro-vision')


    def preprocess(self, uploaded_file):

        if uploaded_file is not None:

            bytes_data = uploaded_file.getvalue()

            image_parts = [
                {
                    "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                    "data": bytes_data
                }
            ]

            return image_parts

    def get_text(self, input, image, prompt):
        try:
            
            response = self.model.generate_content([input, image[0], prompt])

            return response.text

        except Exception as error:
            logging.error(error)
            return None

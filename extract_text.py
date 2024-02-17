import os
import logging
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai



class ExtractText:
    def __init__(self) -> None:
        
        genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro-vision')


    def get_text(self, input, image, prompt):
        try:
            
            response = self.model.generate_content([input, image[0], prompt])

            return response.text

        except Exception as error:
            logging.error(error)
            return None

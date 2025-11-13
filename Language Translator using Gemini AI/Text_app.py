# streamlit_app.py

import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# --- Configuration ---
# Replace YOUR_API_KEY_HERE with your actual Google Gemini API key
GOOGLE_API_KEY = "AIzaSyCtatUjdWNJyM0EFnb-81MA8CkR3EfPm_c"

# Set API key as environment variable
os.environ["GOOGLE_GENAI_API_KEY"] = GOOGLE_API_KEY

# --- Streamlit UI ---
st.set_page_config(page_title="Gemini AI Language Translator", page_icon="🤖")

st.title("Language Translator using Gemini AI")

# --- Text Input ---
text_to_translate = st.text_area("Enter text in English:")

# --- Translate Button ---
if st.button("Click to Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            # Initialize Model
            model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

            # Create prompt
            system_template = "Translate the following English text to Telugu:"
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", system_template),
                ("user", "{text_to_translate}")
            ])

            prompt = prompt_template.invoke({"text_to_translate": text_to_translate})

            # Generate translation
            response = model.invoke(prompt)
            translated_text = response.content

            # Display result
            st.success("Translation Complete!")
            st.text_area("Translated Text (Telugu):", translated_text, height=150)

        except Exception as e:
            st.error(f"Error: {e}")
st.markdown("<div class='footer'>Developed by Aneelkumar Muppana</div>", unsafe_allow_html=True)
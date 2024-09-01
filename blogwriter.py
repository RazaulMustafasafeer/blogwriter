import google.generativeai as genai
import os
import streamlit as st
import json
from dotenv import load_dotenv

# Add CSS for styling and background image
st.markdown(
    """
    <style>
    body {
        background-image: url("https://c4.wallpaperflare.com/wallpaper/621/301/89/macos-mojave-night-wallpaper-preview.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stMarkdown {
        color: #333333;
    }
    * {
        font-family: 'Courier New', monospace;
    }
    textarea {
        background-color: #e6f2ff;
        color: #333333;
        font-family: 'Courier New', monospace;
        border-radius: 5px;
    }
    .stMarkdown h3 {
        background-color: #b3c6ff;
        color: #000000;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

load_dotenv()

api_key = os.getenv('my_api_key')

# Configure the API key
genai.configure(api_key=api_key)

def generate_product_description(product_details, model_name):
    # Create a generative model instance using the specified model name
    model = genai.GenerativeModel(model_name=model_name)

    # Generate content using the product details
    response = model.generate_content([product_details])

    return response.text

# Load the JSON file containing model information
with open(r'C:\Users\Razac\Desktop\blogwriter\blogwriter-434317-295c545d17d6.json', 'r') as f:
    model_info = json.load(f)

# Extract the desired model name from the JSON file
model_name = model_info.get('model_name', 'gemini-1.5-flash')

# Streamlit interface
st.title("Product Description Writer")
st.write("Enter product details below to generate a compelling product description:")

# Text input for product details
product_details = st.text_area("Product Details", placeholder="Enter product features, specifications, etc.")

if st.button("Generate Description"):
    if product_details.strip() != "":
        # Generate and display the product description using the specified model
        description = generate_product_description(product_details, model_name)
        st.write("### Generated Product Description:")
        st.write(description)
    else:
        st.write("Please enter product details to generate a description.")
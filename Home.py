import streamlit as st
from PIL import Image


# Set page config
st.set_page_config(page_title="🔍 Spam Email Detection", page_icon="📧", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main { text-align: center; }
        .stButton>button { background-color: #FF4B4B; color: white; font-size: 18px; padding: 10px 24px; }
        .stButton>button:hover { background-color: #000000; }
        .title { font-size: 36px; font-weight: bold; color: #FF4B4B; }
        .subtitle { font-size: 20px; color: #333333; margin-bottom: 20px; margin-top:0px; }
        .info-text { font-size: 18px; color: #555555; }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------  ST.SIDEBAR ---------------------------------------------------------------------
# Sidebar Description
st.sidebar.subheader("📖 About the App")
st.sidebar.write("This app detects spam emails using a trained machine learning model. Simply enter an email, and the app will classify it as Spam or Not Spam.")

st.sidebar.markdown("---")  # Adds a horizontal line
st.sidebar.subheader("📌 Links:")

# External Links
st.sidebar.markdown("[👨🏻‍💻 Portfolio ](https://manish7272.github.io/)")
st.sidebar.markdown("[🌐 Linkedin ](https://www.linkedin.com/in/manish-gupta-1083761b1/)")
st.sidebar.markdown("[💻 GitHub Repository](https://github.com/Manish7272)")

# --------------------------------------------------------------- HOME --------------------------------------------------------------------------------------------

# Home Page Content
st.markdown("<h1 class='title'>📧 Spam Email Detection App</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Protect yourself from spam and phishing emails.</h3>", unsafe_allow_html=True)

# --------------------------
# Load and resize image
image = Image.open("images/spam.jpg")  # Load the image
image = image.resize((600, 250))  # Resize to desired dimensions (width, height)

# Display the resized image
st.image(image, use_column_width=False)  # Set 'use_column_width=True' for full width
# -------------------------

st.markdown(
    "<p class='info-text'>This app helps you detect spam emails using a machine learning model. "
    "Simply enter an email message, and the model will classify it as Spam or Not Spam.</p>",
    unsafe_allow_html=True
)


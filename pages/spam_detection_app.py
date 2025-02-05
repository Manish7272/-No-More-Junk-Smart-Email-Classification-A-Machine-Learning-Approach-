import streamlit as st
import joblib
from PIL import Image
import numpy as np

# Set page config
st.set_page_config(page_title="🔍 Spam Email Detection", page_icon="📧", layout="centered")

# Load the saved model and vectorizer
model = joblib.load("trained_models/model.pkl")
vectorizer = joblib.load("trained_models/vectorizer.pkl")


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
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Set up the Streamlit app
st.title("🔍 Spam Email Detection App")
st.write("📧 Spam Email Detection App is a machine learning-based web application designed to classify emails as Spam or Not Spam using a trained deep learning model. This app helps users identify unwanted or malicious emails, protecting them from phishing attempts and spam messages.")
# --------------------------
# Load and resize image
image = Image.open("images/spamming.jpg")  # Load the image
image = image.resize((600, 150))  # Resize to desired dimensions (width, height)

# Display the resized image
st.image(image, use_column_width=False)  # Set 'use_column_width=True' for full width
# -------------------------

# Input text box for user input
user_input = st.text_area("Enter your text here:", placeholder = "Type your email content here...")

# Predict button
if st.button("Predict"):
    # Check if the input is valid
    if user_input.strip() == "":
        st.error("Please enter some text.")
    else:
        # Transform the input text using the vectorizer
        input_features = vectorizer.transform([user_input])

        # Make a prediction
        prediction = model.predict(input_features)

        # Display the prediction
        st.write("Prediction:")
        if prediction[0] == 1:
            st.success("🚨 This email is **Spam**!")
        else:
            st.warning("✅ This email is **Not Spam**.")
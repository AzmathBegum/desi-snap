import streamlit as st
from PIL import Image
import gspread
from io import BytesIO
import base64
from google.oauth2.service_account import Credentials

# --- Google Sheets Setup ---
try:
    # Define the required scopes for Google Sheets and Drive
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Authenticate with the credentials file
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    
    # Authorize gspread with the credentials
    gc = gspread.authorize(creds)
    
    # Open the spreadsheet by its name.
    # IMPORTANT: Make sure this name is an EXACT match to your Google Sheet.
    worksheet = gc.open("swecha-project").sheet1
    st.info("Connected to Google Sheets!")
except Exception as e:
    st.error(f"Could not connect to Google Sheets. Please check your credentials and sheet name. Error: {e}")
    st.stop()


# --- Streamlit App ---
st.title("Desi Snap: Share Your World")
st.write("Upload a photo of a local monument, dish, or tradition and add a description in your language.")

uploaded_file = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])
user_text = st.text_area("Add a description:", height=150, help="Describe the image in your native language.")

if st.button("Submit"):
    if uploaded_file is not None and user_text:
        try:
            # Read the image and encode it to base64
            image_bytes = uploaded_file.read()
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            
            # Create a row with the image data and description
            row = [image_base64, user_text]
            
            # Append the row to your Google Sheet
            worksheet.append_row(row)
            
            st.success("Thank you for your contribution!")
            
            # Display the uploaded image
            st.subheader("Your Contribution:")
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption=user_text, use_container_width=True)
            
            st.info("Your data has been successfully saved to our database.")
        except Exception as e:
            st.error(f"An error occurred while saving your data. Error: {e}")
    else:
        st.warning("Please upload a photo and add a description before submitting.")

st.markdown("---")
st.write("In a real app, a photo hosting service would be used, and the image URL would be saved instead of the image data itself.")
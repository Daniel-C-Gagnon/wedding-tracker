import streamlit as st
from supabase import create_client

# Supabase setup
url = st.secrets["supabase_url"]
key = st.secrets["supabase_service_key"]
supabase = create_client(url, key)

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Wedding Tracker Login")

# Form for login
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    try:
        result = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if result.user:
            st.session_state["user"] = result.user
            st.success(f"Welcome {result.user.user_metadata.get('display_name', '')}!")
            st.switch_page("home.py")  # redirect to home after login
        else:
            st.error("Login failed. Please check your credentials.")
    except Exception as e:
        st.error("Login error.")

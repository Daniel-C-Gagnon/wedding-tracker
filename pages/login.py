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
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if response.session:
            st.session_state["user"] = response.user
            st.success("✅ Login successful!")

            # Optional: fetch display name from your 'profiles' table
            profile_resp = supabase.table("profiles").select("display_name").eq("id", response.user.id).execute()
            name = profile_resp.data[0]["display_name"] if profile_resp.data else "User"
            st.success(f"🎉 Welcome, {name}!")

            st.switch_page("home.py")  # Redirect to home
        else:
            st.error("Login failed. Please check your credentials.")

    except Exception as e:
        st.error("❌ Login error.")
        st.exception(e)  # Shows the actual error in dev

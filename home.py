import streamlit as st

st.set_page_config(page_title="Welcome", layout="centered")

st.title("💍 Welcome to Our Wedding Tracker 💍")
st.markdown("#### A private space to track our love & savings journey 💰❤️")

# Display your image (local or remote)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("unnamed.jpg", caption="Saving up for the big day!", width=300)


st.markdown("### 👇 Navigate using the sidebar to:")
st.markdown("- 💰 View and update our savings")
st.markdown("- 📅 (Coming soon) Track upcoming wedding payments")

st.markdown("---")
st.caption("Only accessible by us 💌")

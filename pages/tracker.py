import streamlit as st
from supabase import create_client, Client
from datetime import datetime, timezone

if "user" not in st.session_state:
    st.warning("🔐 You must be logged in to access this page.")
    st.stop()

# --- Supabase config ---
url = st.secrets["supabase_url"]
key = st.secrets["supabase_service_key"]
supabase: Client = create_client(url, key)


# --- Page setup ---
st.set_page_config(page_title="Wedding Savings Tracker", layout="centered")
st.title("💍 Wedding Savings Tracker")

# --- Input area ---
st.markdown("### ➕ Add to savings")
amount = st.number_input("Amount ($)", value= 0.00, step=10.00, format="%.2f")

# --- Setting user id, will automate later __
user_id = "a3bd384f-191b-46d2-9172-6e67ab5e6592"  # Dan's UUID


if st.button("Add Contribution"):
    if amount < 0.01:
        st.warning("⚠️ Value must be greater than or equal to $0.01")
    else:
        # Insert into Supabase
        supabase.table("contributions").insert({
            "amount": round(amount, 2),
            "user_id": user_id,
            "date_added": datetime.now(timezone.utc).strftime('%Y-%m-%d')
        }).execute()
        st.success(f"🚀 Successfully added ${amount:.2f} to your wedding savings! 🚀")
        st.rerun()

# --- Fetch data from Supabase ---
response = supabase.table("contributions_view").select("*").execute()
rows = response.data if response.data else []

# --- Compute total ---
total = sum([row["amount"] for row in rows])

# --- Display total ---
st.markdown("## 🪙 Total Saved")
st.metric(label="Total Wedding Savings", value=f"${total:.2f}")

# --- Display history ---
st.markdown("## 📄 Contribution History")

if rows:
    # Sort by date_added descending
    sorted_rows = sorted(rows, key=lambda x: x["date_added"], reverse=True)
    st.dataframe(sorted_rows)
else:
    st.write("No contributions yet. Start saving!")

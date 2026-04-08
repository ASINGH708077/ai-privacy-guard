import streamlit as st
import sqlite3

st.set_page_config(page_title="AI Privacy Guard", layout="centered")

st.title("🔐 AI Privacy Guard System")

st.write("Enter a website URL to check privacy risks:")

url = st.text_input("Website URL")

if st.button("Check"):
    if url:
        st.success(f"Analyzing {url}...")

        # Dummy analysis (basic)
        if "https" in url:
            st.info("✅ Secure connection (HTTPS detected)")
        else:
            st.warning("⚠️ Not secure (No HTTPS)")

        st.write("🔍 Privacy Risk: LOW (Demo Result)")
    else:
        st.error("Please enter a URL")

st.write("---")
st.caption("Developed by AI Privacy Guard")

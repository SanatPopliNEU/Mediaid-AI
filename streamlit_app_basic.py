#!/usr/bin/env python3
"""
Direct Streamlit Entry Point for Google App Engine
"""
import os
import streamlit as st

# Configure Streamlit for App Engine
st.set_page_config(
    page_title="MediAid AI",
    page_icon="🏥"
)

def main():
    st.title("🏥 MediAid AI - Medical Assistant")
    st.success("✅ Successfully deployed on Google Cloud Platform!")
    
    st.write("### System Info")
    st.write(f"Port: {os.environ.get('PORT', '8080')}")
    st.write(f"Python Version: {os.sys.version}")
    
    st.balloons()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
MediAid AI - Simple Test App for Google Cloud Deployment
"""

import streamlit as st
import os

# Basic configuration
st.set_page_config(
    page_title="MediAid AI",
    page_icon="🏥",
    layout="wide"
)

# Main app
def main():
    st.title("🏥 MediAid AI - Medical Assistant")
    st.write("Welcome to MediAid AI - Your Intelligent Medical Assistant!")
    
    st.subheader("🚀 Deployment Test")
    st.success("✅ Application successfully deployed to Google Cloud!")
    
    st.subheader("🔧 System Information")
    st.write(f"**Python Version:** {os.sys.version}")
    st.write(f"**Streamlit Version:** {st.__version__}")
    st.write(f"**Port:** {os.environ.get('PORT', '8080')}")
    
    st.subheader("🎯 Features Coming Soon")
    st.info("""
    - 🔍 Medical Information Search
    - 📋 Prescription Analysis  
    - 🤖 AI-Powered Health Insights
    - 📊 Health Risk Assessment
    - 📄 Document OCR Processing
    """)
    
    st.subheader("👨‍💻 About")
    st.write("""
    **MediAid AI** is an advanced medical assistant application built with:
    - **Streamlit** for the web interface
    - **OpenAI GPT** for intelligent responses
    - **FAISS** for vector search
    - **Google Cloud Platform** for hosting
    
    Developed by **Sanat Popli** for the Prompt Engineering & AI course.
    """)

if __name__ == "__main__":
    main()

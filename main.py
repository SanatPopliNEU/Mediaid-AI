#!/usr/bin/env python3
"""
MediAid AI - Google Cloud App Engine Entry Point
Optimized Streamlit application for Google Cloud deployment
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Main entry point for Google App Engine"""
    
    # Set environment variables for production
    os.environ["STREAMLIT_SERVER_PORT"] = os.environ.get("PORT", "8080")
    os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    
    # Optimize for cloud deployment
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"
    
    # Get the port from environment (App Engine provides this)
    port = os.environ.get("PORT", "8080")
    
    # Run Streamlit application
    streamlit_cmd = [
        sys.executable, "-m", "streamlit", "run",
        "ultra_simple.py",  # Ultra simple test app
        "--server.port", port,
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ]
    
    print(f"🚀 Starting MediAid AI on port {port}")
    print(f"📝 Command: {' '.join(streamlit_cmd)}")
    
    # Execute Streamlit
    subprocess.run(streamlit_cmd)

if __name__ == "__main__":
    main()

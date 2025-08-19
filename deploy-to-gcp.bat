@echo off
REM MediAid AI - Google Cloud Deployment Script
REM Run this after Google Cloud SDK installation

echo 🚀 MediAid AI - Google Cloud Deployment Setup
echo ================================================

echo.
echo 📝 Step 1: Initialize Google Cloud CLI
echo Run: gcloud init
echo (Select your account and create/select project)
echo.

echo 📝 Step 2: Enable required APIs
echo gcloud services enable appengine.googleapis.com
echo gcloud services enable cloudbuild.googleapis.com
echo gcloud services enable secretmanager.googleapis.com
echo.

echo 📝 Step 3: Initialize App Engine
echo gcloud app create --region=us-central1
echo.

echo 📝 Step 4: Store OpenAI API Key
echo echo "YOUR_OPENAI_API_KEY" ^| gcloud secrets create openai-api-key --data-file=-
echo.

echo 📝 Step 5: Deploy Application
echo gcloud app deploy app.yaml
echo.

echo 📝 Step 6: Open Your App
echo gcloud app browse
echo.

echo ✅ Your MediAid AI will be live on Google Cloud!
echo 🌐 Professional URL for portfolio and demos
echo 💰 Free tier hosting for your project

pause

# 🚀 MediAid AI - Google Cloud Deployment Guide

## 📋 **Prerequisites Completed**
✅ Google Cloud free trial account  
✅ Google Cloud SDK installed  
✅ App Engine configuration files created  
✅ Requirements optimized for cloud deployment  

## 🔧 **Next Steps (Run these commands in order):**

### **1. Initialize Google Cloud CLI**
```bash
# Open a new PowerShell window after SDK installation
gcloud init

# Select your Google account and project
# Create a new project if needed: mediaid-ai-[random-id]
```

### **2. Enable Required APIs**
```bash
# Enable App Engine API
gcloud services enable appengine.googleapis.com

# Enable Cloud Build API (for deployment)
gcloud services enable cloudbuild.googleapis.com

# Enable Secret Manager API (for API keys)
gcloud services enable secretmanager.googleapis.com
```

### **3. Initialize App Engine**
```bash
# Initialize App Engine in your project
gcloud app create --region=us-central1

# Note: Choose a region close to your users
# us-central1 is usually good for North America
```

### **4. Store Your OpenAI API Key Securely**
```bash
# Create a secret for your OpenAI API key
echo "your-actual-openai-api-key-here" | gcloud secrets create openai-api-key --data-file=-

# Grant App Engine access to the secret
gcloud secrets add-iam-policy-binding openai-api-key --member="serviceAccount:your-project@appspot.gserviceaccount.com" --role="roles/secretmanager.secretAccessor"
```

### **5. Prepare Large Files for Cloud Storage**
```bash
# Create a Cloud Storage bucket for your data files
gsutil mb gs://mediaid-ai-data-[your-project-id]

# Upload your FAISS index and medical data
gsutil cp rag_data/medical_embeddings.index gs://mediaid-ai-data-[your-project-id]/
gsutil cp rag_data/medical_embeddings_metadata.json gs://mediaid-ai-data-[your-project-id]/
gsutil cp models/*.pkl gs://mediaid-ai-data-[your-project-id]/models/
```

### **6. Deploy to App Engine**
```bash
# Deploy your application
gcloud app deploy app.yaml

# Deploy will take 5-10 minutes
# You'll get a URL like: https://your-project.uc.r.appspot.com
```

### **7. View Your Deployed App**
```bash
# Open your deployed application
gcloud app browse

# View logs
gcloud app logs tail -s default
```

## 💰 **Free Tier Limits & Cost Management:**

### **App Engine Free Tier (Daily Quotas):**
- ✅ **28 frontend instance hours/day** (enough for development/demo)
- ✅ **1GB outbound bandwidth/day**
- ✅ **1GB Cloud Storage** (free tier)
- ✅ **5GB Cloud Build minutes/month**

### **Cost Optimization Tips:**
1. **Use automatic scaling** with min_instances: 0
2. **Set spending alerts** in Google Cloud Console
3. **Monitor usage** in Cloud Console
4. **Use Cloud Storage** for large files instead of bundling

## 🔧 **Configuration Files Explained:**

### **app.yaml**
- Runtime configuration for App Engine
- Environment variables for your app
- Scaling and resource settings
- Health check configuration

### **requirements-gcp.txt**
- Cloud-optimized Python dependencies
- Smaller package sizes for faster deployment
- Google Cloud specific libraries

### **main.py**
- Entry point for App Engine
- Configures Streamlit for cloud deployment
- Handles port and address configuration

### **.gcloudignore**
- Files to exclude from deployment
- Reduces deployment size and time
- Keeps sensitive files local

## 🚨 **Important Security Notes:**

### **API Key Management:**
- ❌ **Never** put API keys directly in app.yaml
- ✅ **Use** Google Secret Manager for sensitive data
- ✅ **Set** proper IAM permissions

### **Environment Variables:**
```yaml
# In app.yaml, reference secrets:
env_variables:
  OPENAI_API_KEY_SECRET: "projects/your-project/secrets/openai-api-key/versions/latest"
```

## 📊 **Monitoring Your Deployment:**

### **Useful Commands:**
```bash
# Check app status
gcloud app versions list

# View logs in real-time
gcloud app logs tail -s default

# Check quotas and usage
gcloud app quota --help

# Set traffic allocation
gcloud app services set-traffic default --splits=v1=100
```

### **Google Cloud Console URLs:**
- **App Engine Dashboard**: https://console.cloud.google.com/appengine
- **Logs Viewer**: https://console.cloud.google.com/logs
- **Billing**: https://console.cloud.google.com/billing
- **IAM & Security**: https://console.cloud.google.com/iam-admin

## 🎯 **Expected Results:**

After successful deployment, you'll have:
- ✅ **Public URL** for your MediAid AI application
- ✅ **Automatic scaling** based on traffic
- ✅ **Professional deployment** suitable for portfolios
- ✅ **Free hosting** within GCP free tier limits
- ✅ **Global accessibility** for demos and submissions

## 🆘 **Troubleshooting:**

### **Common Issues:**
1. **Large deployment size**: Use .gcloudignore to exclude unnecessary files
2. **Memory issues**: Optimize requirements, use Cloud Storage for data
3. **API key errors**: Check Secret Manager permissions
4. **Timeout issues**: Increase instance startup timeout in app.yaml

### **Support Resources:**
- Google Cloud Documentation: https://cloud.google.com/appengine/docs
- App Engine Python Runtime: https://cloud.google.com/appengine/docs/standard/python3
- Streamlit on GCP: https://docs.streamlit.io/deploy/tutorials

---

**🚀 Ready to deploy your MediAid AI to the cloud and showcase it globally!**

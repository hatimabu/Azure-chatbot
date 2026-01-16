# Infrastructure Deployment Guide

**⚠️ READ THIS FIRST:** You don't need this yet! This folder is for when you're ready to deploy your chatbot to Azure and make it public.

## 🎯 When Should You Use This?

Deploy when you:
- ✅ Understand how the local chatbot works
- ✅ Have tested it thoroughly locally
- ✅ Want to make it accessible 24/7
- ✅ Want others to use it
- ✅ Are ready to spend ~$30-50/month on Azure

**Don't deploy if:** You're still learning or testing locally!

## 💰 Cost Estimate

### Minimal Setup (What we're deploying):
- **Azure Functions:** $0-5/month (1M free calls, then $0.20 per million)
- **Azure Cosmos DB:** $25/month (serverless, starts free)
- **Azure Storage:** $1-2/month
- **Application Insights:** Free tier (5GB/month)

**Total:** ~$30-35/month for light usage

### Free Tier Reality:
- First month: $200 Azure credit (FREE)
- Functions: 1 million calls/month FREE
- Storage: First 5GB FREE
- You can run 2-3 months nearly FREE if usage is low

## 🏗️ What Gets Deployed

```
Azure Cloud
├── Resource Group (container for everything)
├── Azure Functions (runs your chatbot code)
├── Cosmos DB (stores conversations)
├── Storage Account (files, backups)
└── Application Insights (monitoring, logs)
```

## 📋 Prerequisites

Before deploying, you need:

1. **Azure Account**
   - Sign up: https://azure.microsoft.com/free/
   - Get $200 free credit for first month

2. **Azure CLI** (command line tool)
   ```bash
   # Mac
   brew install azure-cli
   
   # Windows
   # Download from: https://aka.ms/installazurecliwindows
   
   # Linux
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

3. **Terraform** (infrastructure tool)
   ```bash
   # Mac
   brew install terraform
   
   # Windows
   # Download from: https://www.terraform.io/downloads
   
   # Linux
   wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
   ```

4. **Your OpenAI API Key** (you already have this!)

## 🚀 Deployment Steps (When Ready)

### Step 1: Login to Azure
```bash
# Login
az login

# Verify you're logged in
az account show

# Set subscription (if you have multiple)
az account set --subscription "Your-Subscription-Name"
```

### Step 2: Initialize Terraform
```bash
cd infra/azure/terraform

# Initialize
terraform init

# See what will be created (no changes yet)
terraform plan
```

### Step 3: Deploy!
```bash
# This creates everything in Azure
terraform apply

# Type 'yes' when prompted
# Wait 5-10 minutes
```

### Step 4: Configure Your Function App
```bash
# Get your function app name from terraform output
FUNCTION_APP_NAME=$(terraform output -raw function_app_name)

# Set your OpenAI API key
az functionapp config appsettings set \
  --name $FUNCTION_APP_NAME \
  --resource-group islamic-chatbot-rg \
  --settings "OPENAI_API_KEY=your-key-here"
```

### Step 5: Deploy Your Code
```bash
# From project root
cd ../../..

# Install Azure Functions Core Tools if needed
npm install -g azure-functions-core-tools@4

# Deploy
func azure functionapp publish $FUNCTION_APP_NAME
```

### Step 6: Test It!
```bash
# Get your function URL
terraform output function_app_url

# Test with curl
curl -X POST https://your-app.azurewebsites.net/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the five pillars of Islam?"}'
```

## 🎉 You're Live!

Your chatbot is now:
- ✅ Running 24/7
- ✅ Accessible from anywhere
- ✅ Auto-scaling
- ✅ Being monitored

Share your URL with others!

## 🔧 Managing Your Deployment

### View Logs
```bash
# Real-time logs
az functionapp log tail --name $FUNCTION_APP_NAME --resource-group islamic-chatbot-rg

# Or use Azure Portal: portal.azure.com
```

### Update Your Code
```bash
# Make changes locally, then:
func azure functionapp publish $FUNCTION_APP_NAME
```

### Check Costs
```bash
# View current month costs
az consumption usage list --start-date 2026-01-01 --end-date 2026-01-31
```

### Stop Everything (Pause Costs)
```bash
# Stop the function app (keeps data)
az functionapp stop --name $FUNCTION_APP_NAME --resource-group islamic-chatbot-rg

# Start it again later
az functionapp start --name $FUNCTION_APP_NAME --resource-group islamic-chatbot-rg
```

### Delete Everything
```bash
cd infra/azure/terraform
terraform destroy
# Type 'yes' to confirm
```

## 🐛 Troubleshooting

### "Terraform not found"
Install Terraform: https://www.terraform.io/downloads

### "Azure CLI not found"
Install Azure CLI: https://docs.microsoft.com/cli/azure/install-azure-cli

### "Insufficient permissions"
Make sure you're logged in: `az login`

### "Resource already exists"
Someone else might have the same name. Edit `variables.tf` and change `project_name`

### "Deployment failed"
Check logs:
```bash
az functionapp log tail --name $FUNCTION_APP_NAME --resource-group islamic-chatbot-rg
```

## 📊 Monitoring Your App

### Azure Portal
1. Go to https://portal.azure.com
2. Find your Resource Group: `islamic-chatbot-rg`
3. Click on your Function App
4. View:
   - Metrics (requests, errors)
   - Logs
   - Performance
   - Costs

### Application Insights
- Click "Application Insights" in portal
- See real-time usage
- Track errors
- Monitor performance

## 🔒 Security Best Practices

1. **Never commit secrets**
   - API keys stay in Azure App Settings
   - Not in code or terraform files

2. **Use Azure Key Vault** (optional, advanced)
   - Uncomment key vault in `main.tf`
   - Store secrets more securely

3. **Enable authentication**
   - Add API keys for your function
   - Prevent unauthorized access

4. **Monitor costs**
   - Set up billing alerts
   - Check weekly

## 📈 Scaling Up

When you're ready to handle more users:

1. **Upgrade Function Plan**
   - Edit `variables.tf`
   - Change to Premium plan

2. **Add CDN**
   - Faster global access
   - Cache responses

3. **Add API Management**
   - Rate limiting
   - Analytics
   - Multiple versions

## 🎓 Learning Resources

- Azure Functions: https://docs.microsoft.com/azure/azure-functions/
- Terraform: https://learn.hashicorp.com/terraform
- Azure Cosmos DB: https://docs.microsoft.com/azure/cosmos-db/

## ❓ Common Questions

**Q: Can I deploy to AWS or Google Cloud instead?**
A: Yes! But you'd need different terraform files. Start with Azure for now.

**Q: Will this work with the advanced version later?**
A: Yes! This is designed to grow with your project.

**Q: Can I test deployment without paying?**
A: Yes! Use the $200 free credit. Just remember to destroy resources after testing.

**Q: How do I add a web interface?**
A: We'll add that later. For now, this is just the API.

## 🎯 Remember

- **No rush** - Deploy when YOU'RE ready
- **Start small** - This basic setup is fine
- **Monitor costs** - Set billing alerts
- **Test locally first** - Make sure everything works
- **Backup your data** - Export Cosmos DB regularly

---

**Need help?** Read through this guide completely before deploying. Most issues are solved by following steps carefully.

**Still stuck?** Check the troubleshooting section or Azure documentation.

**Ready to go?** Start with Step 1 above! 🚀
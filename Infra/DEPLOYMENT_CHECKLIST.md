# Deployment Checklist

Use this checklist when you're ready to deploy. Check off each item!

## 📋 Pre-Deployment (Before You Start)

### Knowledge & Skills
- [ ] You understand how the local chatbot works
- [ ] You've tested it thoroughly locally
- [ ] You've read through the infrastructure files
- [ ] You understand basic Azure concepts
- [ ] You're comfortable with command line

### Prerequisites Installed
- [ ] Azure CLI installed (`az --version`)
- [ ] Terraform installed (`terraform --version`)
- [ ] Azure Functions Core Tools (`func --version`)
- [ ] Python 3.11+ (`python --version`)
- [ ] Git (`git --version`)

### Accounts & Access
- [ ] Azure account created
- [ ] Credit card added (for after free trial)
- [ ] $200 free credit activated (if new account)
- [ ] OpenAI API key obtained
- [ ] OpenAI account has credit ($5 free or paid)

### Financial Preparation
- [ ] Read COST_ESTIMATE.md
- [ ] Budget set: $______/month
- [ ] Billing alerts configured (or planned)
- [ ] Understand you'll be charged (after free tier)
- [ ] Ready to monitor costs daily (first week)

## 🔐 Security Setup

### Before Deployment
- [ ] `.env` file is in `.gitignore`
- [ ] No API keys in code
- [ ] No secrets in terraform files
- [ ] Strong Azure password set
- [ ] 2FA enabled on Azure account

### After Deployment
- [ ] API keys stored in Azure App Settings
- [ ] Access restricted (if needed)
- [ ] Logging enabled
- [ ] Billing alerts configured

## 🚀 Deployment Process

### Step 1: Azure Login
- [ ] Logged in: `az login`
- [ ] Correct subscription selected
- [ ] Subscription verified: `az account show`

### Step 2: Terraform Initialization
- [ ] Navigated to: `infra/azure/terraform`
- [ ] Ran: `terraform init`
- [ ] No errors in initialization
- [ ] Provider plugins downloaded

### Step 3: Infrastructure Review
- [ ] Ran: `terraform plan`
- [ ] Reviewed resources to be created
- [ ] Resource names look correct
- [ ] Location is correct (eastus, westeurope, etc.)
- [ ] No unexpected resources

### Step 4: Deploy Infrastructure
- [ ] Ran: `terraform apply`
- [ ] Typed 'yes' to confirm
- [ ] Waited 5-10 minutes
- [ ] No errors in deployment
- [ ] Outputs displayed successfully

### Step 5: Configure Function App
- [ ] Got function app name from outputs
- [ ] Set OpenAI API key in Azure
- [ ] Verified settings: `az functionapp config appsettings list`
- [ ] API key not visible in logs

### Step 6: Deploy Function Code
- [ ] In project root directory
- [ ] Ran: `func azure functionapp publish <name>`
- [ ] Deployment succeeded
- [ ] No errors in deployment logs

### Step 7: Testing
- [ ] Got function URL from terraform outputs
- [ ] Tested with curl command
- [ ] Got valid response
- [ ] Response makes sense
- [ ] No errors in response

## ✅ Post-Deployment

### Immediate (Within 1 Hour)
- [ ] Health check endpoint works
- [ ] Tested with 3-5 different questions
- [ ] Responses are appropriate
- [ ] No errors in Application Insights
- [ ] Function app shows as running in portal

### First Day
- [ ] Monitored logs for errors
- [ ] Checked costs in Azure portal ($0-1 expected)
- [ ] Tested from different device/location
- [ ] Shared URL with one friend (optional)
- [ ] Verified their request worked

### First Week
- [ ] Checked costs daily
- [ ] Reviewed Application Insights
- [ ] No unexpected errors
- [ ] Performance acceptable
- [ ] Billing alert triggered correctly (if set)

### First Month
- [ ] Reviewed monthly costs
- [ ] Compared actual vs estimated costs
- [ ] Identified any optimization opportunities
- [ ] Decided if keeping deployed or pausing

## 🐛 Troubleshooting Checklist

### If Deployment Fails
- [ ] Checked Azure portal for error messages
- [ ] Reviewed terraform error output
- [ ] Verified all prerequisites installed
- [ ] Tried again after fixing issue
- [ ] Checked Azure service health

### If Function Doesn't Work
- [ ] Verified function app is running
- [ ] Checked Application Insights logs
- [ ] Verified OpenAI API key is set
- [ ] Tested OpenAI key with local chatbot
- [ ] Checked function app configuration

### If Costs Are Unexpected
- [ ] Reviewed Cost Management dashboard
- [ ] Checked for resource leaks
- [ ] Verified scale limits are set
- [ ] Reviewed function execution count
- [ ] Considered pausing/stopping

## 🛑 Emergency Stop

### If Something Goes Wrong
- [ ] Stop function app: `az functionapp stop --name <name> --resource-group <rg>`
- [ ] Check costs immediately
- [ ] Review what went wrong
- [ ] Fix issue before restarting
- [ ] Consider destroying resources if needed

### Complete Teardown
- [ ] Navigate to: `infra/azure/terraform`
- [ ] Run: `terraform destroy`
- [ ] Type 'yes' to confirm
- [ ] Wait for deletion (5 minutes)
- [ ] Verify in Azure portal all resources deleted

## 📊 Success Criteria

You've successfully deployed if:
- [ ] Function app is running
- [ ] Can send requests and get responses
- [ ] Costs are within expected range
- [ ] No errors in logs
- [ ] Can access from anywhere
- [ ] Performance is acceptable

## 🎯 Optional Enhancements

### After Successful Deployment
- [ ] Add custom domain
- [ ] Enable authentication
- [ ] Add rate limiting
- [ ] Integrate Cosmos DB
- [ ] Add web interface
- [ ] Set up CI/CD pipeline
- [ ] Add more monitoring
- [ ] Optimize costs

## 📝 Notes Section

Use this space for your own notes:

**Deployment Date:** _______________

**Function App Name:** _______________

**Function URL:** _______________

**Issues Encountered:**
1. _______________
2. _______________
3. _______________

**Actual First Month Cost:** $_______________

**Lessons Learned:**
- _______________
- _______________
- _______________

---

**Remember:** Take your time. It's better to deploy slowly and correctly than rush and have problems. You can always try again!
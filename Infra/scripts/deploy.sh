#!/bin/bash

# Islamic AI Chatbot - Deployment Script
# This script automates the deployment process
# Run this when you're ready to deploy!

set -e  # Exit on any error

echo "================================================"
echo "Islamic AI Chatbot - Azure Deployment"
echo "================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check prerequisites
echo "Checking prerequisites..."

# Check Azure CLI
if ! command -v az &> /dev/null; then
    print_error "Azure CLI not found. Install it first:"
    echo "  https://docs.microsoft.com/cli/azure/install-azure-cli"
    exit 1
fi
print_status "Azure CLI found"

# Check Terraform
if ! command -v terraform &> /dev/null; then
    print_error "Terraform not found. Install it first:"
    echo "  https://www.terraform.io/downloads"
    exit 1
fi
print_status "Terraform found"

# Check if logged into Azure
if ! az account show &> /dev/null; then
    print_warning "Not logged into Azure. Logging in..."
    az login
fi
print_status "Logged into Azure"

# Get current subscription
SUBSCRIPTION=$(az account show --query name -o tsv)
echo ""
echo "Current subscription: $SUBSCRIPTION"
read -p "Is this correct? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please set the correct subscription:"
    echo "  az account set --subscription 'Your-Subscription-Name'"
    exit 1
fi

# Ask for OpenAI API Key
echo ""
print_warning "You'll need your OpenAI API key"
read -sp "Enter your OpenAI API key: " OPENAI_KEY
echo ""

if [ -z "$OPENAI_KEY" ]; then
    print_error "OpenAI API key is required"
    exit 1
fi

# Navigate to terraform directory
cd "$(dirname "$0")/../azure/terraform"

echo ""
echo "================================================"
echo "Step 1: Initialize Terraform"
echo "================================================"
terraform init

echo ""
echo "================================================"
echo "Step 2: Plan Deployment"
echo "================================================"
echo "Review what will be created..."
terraform plan

echo ""
read -p "Ready to deploy? This will create Azure resources. (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled"
    exit 0
fi

echo ""
echo "================================================"
echo "Step 3: Deploy Infrastructure"
echo "================================================"
echo "This will take 5-10 minutes..."
terraform apply -auto-approve

# Get outputs
echo ""
echo "================================================"
echo "Step 4: Configure Function App"
echo "================================================"
FUNCTION_APP_NAME=$(terraform output -raw function_app_name)
RESOURCE_GROUP=$(terraform output -raw resource_group_name)

print_status "Function App: $FUNCTION_APP_NAME"

# Set OpenAI API key
echo "Setting OpenAI API key..."
az functionapp config appsettings set \
    --name "$FUNCTION_APP_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --settings "OPENAI_API_KEY=$OPENAI_KEY" \
    --output none

print_status "API key configured"

echo ""
echo "================================================"
echo "Step 5: Deploy Function Code"
echo "================================================"

# Go back to project root
cd ../../..

# Check if func CLI is installed
if ! command -v func &> /dev/null; then
    print_warning "Azure Functions Core Tools not found"
    echo "Install it: npm install -g azure-functions-core-tools@4"
    echo ""
    echo "After installing, deploy manually with:"
    echo "  func azure functionapp publish $FUNCTION_APP_NAME"
    echo ""
    echo "Infrastructure is deployed, but you need to deploy code manually."
    exit 0
fi

# Deploy function code
echo "Deploying your chatbot code..."
func azure functionapp publish "$FUNCTION_APP_NAME" --python

echo ""
echo "================================================"
echo "✓ DEPLOYMENT COMPLETE!"
echo "================================================"
echo ""

# Get function URL
FUNCTION_URL=$(cd infra/azure/terraform && terraform output -raw function_app_url)

echo "Your chatbot is live at:"
echo "  $FUNCTION_URL/api/chat"
echo ""
echo "Test it with:"
echo "  curl -X POST $FUNCTION_URL/api/chat \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"message\": \"What are the five pillars of Islam?\"}'"
echo ""
echo "View in Azure Portal:"
echo "  https://portal.azure.com/#resource/subscriptions/$(az account show --query id -o tsv)/resourceGroups/$RESOURCE_GROUP/overview"
echo ""
echo "Monitor logs:"
echo "  az functionapp log tail --name $FUNCTION_APP_NAME --resource-group $RESOURCE_GROUP"
echo ""
echo "================================================"
echo "Remember:"
echo "- Monitor your costs in Azure Portal"
echo "- Set up billing alerts"
echo "- Check Application Insights for usage stats"
echo "================================================"
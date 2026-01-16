# Islamic AI Chatbot - Azure Infrastructure
# This file defines all Azure resources needed to run your chatbot in the cloud
# DON'T RUN THIS YET - Just keep it for when you're ready!

terraform {
  required_version = ">= 1.0"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

# Import variables from variables.tf
variable "project_name" {}
variable "environment" {}
variable "location" {}

# Create names for resources
locals {
  resource_prefix = "${var.project_name}-${var.environment}"
  
  tags = {
    Project     = "Islamic AI Chatbot"
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# Resource Group - Container for all resources
resource "azurerm_resource_group" "main" {
  name     = "${local.resource_prefix}-rg"
  location = var.location
  tags     = local.tags
}

# Storage Account - For function app and file storage
resource "azurerm_storage_account" "main" {
  name                     = replace("${local.resource_prefix}sa", "-", "")
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  
  tags = local.tags
}

# App Service Plan - Serverless (Consumption)
resource "azurerm_service_plan" "main" {
  name                = "${local.resource_prefix}-plan"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = "Y1"  # Y1 = Consumption tier (pay per use)
  
  tags = local.tags
}

# Function App - Where your chatbot code runs
resource "azurerm_linux_function_app" "main" {
  name                       = "${local.resource_prefix}-func"
  resource_group_name        = azurerm_resource_group.main.name
  location                   = azurerm_resource_group.main.location
  service_plan_id            = azurerm_service_plan.main.id
  storage_account_name       = azurerm_storage_account.main.name
  storage_account_access_key = azurerm_storage_account.main.primary_access_key
  
  site_config {
    application_stack {
      python_version = "3.11"
    }
    
    # Allow requests from anywhere
    cors {
      allowed_origins = ["*"]  # Change this to your domain in production
    }
    
    # Enable better performance
    app_scale_limit = 10
  }
  
  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"       = "python"
    "AzureWebJobsStorage"            = azurerm_storage_account.main.primary_connection_string
    "WEBSITE_RUN_FROM_PACKAGE"       = "1"
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.main.instrumentation_key
    
    # These will be set manually after deployment
    # "OPENAI_API_KEY" = "your-key-here"
  }
  
  tags = local.tags
}

# Cosmos DB Account - NoSQL database for conversations
resource "azurerm_cosmosdb_account" "main" {
  name                = "${local.resource_prefix}-cosmos"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  
  consistency_policy {
    consistency_level = "Session"
  }
  
  geo_location {
    location          = azurerm_resource_group.main.location
    failover_priority = 0
  }
  
  # Serverless mode - only pay for what you use
  capabilities {
    name = "EnableServerless"
  }
  
  tags = local.tags
}

# Cosmos DB Database
resource "azurerm_cosmosdb_sql_database" "main" {
  name                = "chatbot"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

# Cosmos DB Container - Stores conversation history
resource "azurerm_cosmosdb_sql_container" "conversations" {
  name                = "conversations"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
  database_name       = azurerm_cosmosdb_sql_database.main.name
  partition_key_paths = ["/conversationId"]
  
  # Automatic cleanup of old conversations (optional)
  default_ttl = 2592000  # 30 days in seconds
}

# Application Insights - Monitoring and logging
resource "azurerm_application_insights" "main" {
  name                = "${local.resource_prefix}-insights"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  application_type    = "web"
  
  tags = local.tags
}

# Outputs - Important info you'll need after deployment
output "function_app_name" {
  value       = azurerm_linux_function_app.main.name
  description = "Name of the Function App"
}

output "function_app_url" {
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
  description = "URL of your chatbot API"
}

output "resource_group_name" {
  value       = azurerm_resource_group.main.name
  description = "Resource group name"
}

output "cosmos_db_endpoint" {
  value       = azurerm_cosmosdb_account.main.endpoint
  description = "Cosmos DB endpoint"
  sensitive   = true
}

output "cosmos_db_key" {
  value       = azurerm_cosmosdb_account.main.primary_key
  description = "Cosmos DB primary key"
  sensitive   = true
}

output "application_insights_key" {
  value       = azurerm_application_insights.main.instrumentation_key
  description = "Application Insights key"
  sensitive   = true
}
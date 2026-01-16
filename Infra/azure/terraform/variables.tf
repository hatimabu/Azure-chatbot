# Variables for Azure Infrastructure
# You can customize these values

variable "project_name" {
  description = "Name of the project (will be used in resource names)"
  type        = string
  default     = "ai-chatbot"
  
  validation {
    condition     = length(var.project_name) <= 20
    error_message = "Project name must be 20 characters or less"
  }
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod"
  }
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "eastus"
  
  # Common regions:
  # eastus, westus, centralus (USA)
  # westeurope, northeurope (Europe)
  # southeastasia, eastasia (Asia)
  # canadacentral (Canada)
  # australiaeast (Australia)
}

# Optional: Uncomment if you want to customize these

# variable "python_version" {
#   description = "Python version for Function App"
#   type        = string
#   default     = "3.11"
# }

# variable "function_app_scale_limit" {
#   description = "Maximum number of function app instances"
#   type        = number
#   default     = 10
# }

# variable "cosmos_ttl_seconds" {
#   description = "Time to live for Cosmos DB documents (seconds)"
#   type        = number
#   default     = 2592000  # 30 days
# }
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.2.0"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  features {}
}

variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "baeaf599-3dbd-4063-a939-8a4dca2de156"
}
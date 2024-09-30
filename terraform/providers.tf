terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.2.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.0.0"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
  }
}

provider "databricks" {
  azure_workspace_resource_id = azurerm_databricks_workspace.this.id
}

data "azurerm_client_config" "current" {}

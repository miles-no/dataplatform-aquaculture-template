terraform {
  backend "azurerm" {
    resource_group_name  = "dev-aquaculture-tf-rg"
    storage_account_name = "aquaculturetfstate"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }

  required_version = ">= 1.5.0"
}

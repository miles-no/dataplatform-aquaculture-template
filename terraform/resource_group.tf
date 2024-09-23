
resource "azurerm_resource_group" "data_platform" {
  name     = "dev-aquaculture-rg"
  location = var.location
}

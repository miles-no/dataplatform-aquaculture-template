
resource "azurerm_data_factory" "data_platform" {
  name                = "dev-aquaculture-df"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
}
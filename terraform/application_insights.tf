# (Optional) Application Insights - For Monitoring
resource "azurerm_application_insights" "apin" {
  name                = "dp-appinsights"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
  application_type    = "web"
}

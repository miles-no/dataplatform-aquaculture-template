resource "azurerm_application_insights" "apin" {
  name                = "dp-appinsights"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
  application_type    = "web"
  workspace_id        = azurerm_log_analytics_workspace.log.id

}

resource "azurerm_log_analytics_workspace" "log" {
  name                = "workspace-test"
  location            =  azurerm_resource_group.data_platform.location
  resource_group_name =  azurerm_resource_group.data_platform.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}
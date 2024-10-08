# App Service Plan
resource "azurerm_service_plan" "func" {
  name                = "dp-func-appserviceplan"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
  os_type             = "Linux"
  sku_name            = "B1"
}

# Function App
resource "azurerm_linux_function_app" "func" {
  name                       = "dev-aquaplatform-func"
  location                   = azurerm_resource_group.data_platform.location
  resource_group_name        = azurerm_resource_group.data_platform.name
  storage_account_name       = azurerm_storage_account.data_lake.name
  storage_account_access_key = azurerm_storage_account.data_lake.primary_access_key
  service_plan_id            = azurerm_service_plan.func.id
  site_config {
    application_insights_connection_string = azurerm_application_insights.apin.connection_string
    application_stack {
      dotnet_version = "8.0"
    }
  }
}

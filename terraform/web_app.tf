resource "azurerm_service_plan" "asp" {
  name                = "aquaplatform-api-asp"
  resource_group_name = azurerm_resource_group.data_platform.name
  location            = azurerm_resource_group.data_platform.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "web_app" {
  name                = "aquaplatform-api-app"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
  service_plan_id     = azurerm_service_plan.asp.id

  site_config {
    app_command_line = ""
    application_stack {
      docker_registry_url      = "https://${azurerm_container_registry.acr.login_server}"
      docker_registry_password = azurerm_container_registry.acr.admin_password
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_image_name        = var.container_image
    }
  }

  app_settings = {
    "ConnectionStrings__BlobStorage" : "DefaultEndpointsProtocol=https;AccountName=${azurerm_storage_account.data_lake.name};AccountKey=${azurerm_storage_account.data_lake.primary_access_key};EndpointSuffix=core.windows.net"
    "DOCKER_ENABLE_CI" = true
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "aquadpcontainerregistry"
  resource_group_name = azurerm_resource_group.data_platform.name
  location            = azurerm_resource_group.data_platform.location
  sku                 = "Basic"
  admin_enabled       = true
}

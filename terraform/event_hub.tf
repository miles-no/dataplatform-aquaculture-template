
resource "azurerm_eventhub_namespace" "this" {
  name                = "dev-aquaplatform-ehn"
  location            = azurerm_resource_group.data_platform.location
  resource_group_name = azurerm_resource_group.data_platform.name
  sku                 = "Standard"
  capacity            = 1
}

resource "azurerm_eventhub" "this" {
  name                = "dev-aquaplatform-eventhub"
  namespace_name      = azurerm_eventhub_namespace.this.name
  resource_group_name = azurerm_resource_group.data_platform.name
  partition_count     = 2
  message_retention   = 1
}

resource "azurerm_eventhub_namespace_authorization_rule" "this" {
  name                = "function-authorize-rule"
  namespace_name      = azurerm_eventhub_namespace.this.name
  resource_group_name = azurerm_resource_group.data_platform.name
  listen              = false
  send                = true
  manage              = false
}

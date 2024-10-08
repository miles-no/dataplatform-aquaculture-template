resource "azurerm_key_vault" "dataplatform" {
  name                        = "havsbruk-dataplatform-kv"
  location                    = azurerm_resource_group.data_platform.location
  resource_group_name         = azurerm_resource_group.data_platform.name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = true

  sku_name = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    key_permissions = [
      "Get",
    ]

    secret_permissions = [
      "Get",
      "Set",
      "List"
    ]

    storage_permissions = [
      "Get",
    ]
  }
}

# Key Vault Secret
resource "azurerm_key_vault_secret" "storage_account_key" {
  name         = "storage-account-key"
  value        = azurerm_storage_account.data_lake.primary_access_key
  key_vault_id = azurerm_key_vault.dataplatform.id
}



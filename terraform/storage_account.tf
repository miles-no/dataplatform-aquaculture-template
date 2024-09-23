
#Add a Delete Lock to the Storage Account
resource "azurerm_management_lock" "storage_lock" {
  name       = "storage-delete-lock"
  scope      = azurerm_storage_account.data_lake.id
  lock_level = "CanNotDelete"
}

resource "azurerm_storage_account" "data_lake" {
  name                     = "devaquaplatformst01"
  resource_group_name      = azurerm_resource_group.data_platform.name
  location                 = azurerm_resource_group.data_platform.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "data_lake" {
  name               = "datalake"
  storage_account_id = azurerm_storage_account.data_lake.id
}

resource "azurerm_storage_data_lake_gen2_path" "data_platform" {
  path               = "data_lake"
  filesystem_name    = azurerm_storage_data_lake_gen2_filesystem.data_lake.name
  storage_account_id = azurerm_storage_account.data_lake.id
  resource           = "directory"
}

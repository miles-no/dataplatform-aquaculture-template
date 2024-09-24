

resource "azurerm_databricks_workspace" "this" {
  name                = "devaquaplatformdbx"
  resource_group_name = azurerm_resource_group.data_platform.name
  location            = azurerm_resource_group.data_platform.location
  sku                 = "standard"
}


resource "databricks_cluster" "this" {
  cluster_name            = "standard"
  spark_version           = "7.3.x-scala2.12"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 30
  num_workers             = 2
}

resource "databricks_secret_scope" "this" {
  name = "terraform-demo-scope"
  keyvault_metadata {
    resource_id = azurerm_key_vault.example.id
    dns_name    = azurerm_key_vault.example.vault_uri
  }
}

resource "databricks_repo" "data_platform" {
  url = var.github_repo
}

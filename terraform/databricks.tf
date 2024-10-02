

resource "azurerm_databricks_workspace" "this" {
  name                = "devaquaplatformdbx"
  resource_group_name = azurerm_resource_group.data_platform.name
  location            = azurerm_resource_group.data_platform.location
  sku                 = "standard"
}

data "databricks_spark_version" "this" {
  latest = true
}
resource "databricks_cluster" "this" {
  cluster_name            = "standard"
  spark_version           = data.databricks_spark_version.this.id
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 30
  num_workers             = 2
}

resource "databricks_secret_scope" "data_platform" {
  name                     = "terraform-created-scope"
  initial_manage_principal = "users"

  keyvault_metadata {
    resource_id = azurerm_key_vault.dataplatform.id
    dns_name    = azurerm_key_vault.dataplatform.vault_uri
  }
}

resource "databricks_repo" "data_platform" {
  url = var.github_repo
}

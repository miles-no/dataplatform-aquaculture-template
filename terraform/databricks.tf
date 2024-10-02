

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

resource "databricks_repo" "data_platform" {
  url = var.github_repo
}

resource "databricks_secret" "publishing_api" {
  key          = "scope-storage-account-key"
  string_value = azurerm_storage_account.data_lake.primary_access_key
  scope        = databricks_secret_scope.data_platform.id
}

resource "databricks_secret_scope" "data_platform" {
  name                     = "terraform-created-scope"
  initial_manage_principal = "users"
}

# AquaCulture Data Platform

## Setup Guide

### 1. Setup a resource group for the terraform state 

In order to properly manage the terraform .state file, one creates a resource group in azure with a storage account to hold the terraform state. 
This is then referenced in the `terraform/backend.tf` clause in the terraform configuration. If you have created a new resource group and storage account, you must change the names in the `†erraform/backend.tf` to match the names of the resources you created. 

### 2. Run terraform configuration in order to populate the cloud with the required resources. 

1. az login
2. terraform init
3. terraform plan
4. terraform apply

### 3. Add Azure Container Registry secrets into Github actions 

In order for the api docker image to be published to the Azure Container Registry (ACR) we need to add three variables to the github repo. These variables are listed below, and can be found in the azure portal after navigating

1. ACR_PASSWORD
2. ACR_USERNAME 
3. ARC_SERVER (the whole path to the arc, including the .azurecr.io suffix

### 4. Run the Github Actions to publish 

Navigate to the `Actions` tab in Github, and check if the actions script for publishing an image to Azure Container Registry have run successfully. If not, then restart it in order to publish the code to the registry 

## Local Development

1. Create a file called `api/AquaApi/appsettings.Development.json`. This must be .gitignored. Add a variable `ConnectionStrings:BlobStorage` storage connection string to the appsettings.
2. The connection string must be on the format: `DefaultEndpointsProtoco=https;AccountName=<your-storage-account>;AccountKey=<storage-key>;EndpointSuffix=core.windows.net"`

## Overview

This project is a template for a data platform designed for small and medium-large aquaculture companies in Norway. It leverages the power of Azure, Databricks, and Terraform to provide a scalable and efficient solution for managing and transforming data. The platform follows the **Medallion Architecture** and fetches data daily from [api.havvarsel.no](https://api.havvarsel.no).

## Architecture

- **Azure Databricks Architecture**: This platform is built on the Azure Databricks architecture, providing a unified analytics framework that integrates with Azure services. You can learn more about Azure Databricks architecture [here](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture).
  ![image](https://github.com/user-attachments/assets/66c5ac82-26cc-4eef-a3a5-b471881acac2)

- **Medallion Architecture**: The platform transforms data following the Medallion Architecture, enabling efficient and scalable data processing. Learn more about Medallion Architecture [here](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion). 

## Data Flow

1. **Data Source**: Every day, new data is fetched from the public API at [api.havvarsel.no](https://api.havvarsel.no).
2. **Transformation**: The raw data is transformed using Databricks' Medallion Architecture, processing it in stages (Bronze, Silver, Gold).
3. **Reporting**: The transformed data is available through a Power BI report, which can be accessed [here](#). (Add link to your Power BI report)

## Deployment

This project uses Terraform to automate the deployment of infrastructure and resources on Azure. To get started with setting up the platform, follow the official Terraform documentation for running up a new project [here](https://developer.hashicorp.com/terraform/cli/run).

## Prerequisites

- Azure Subscription
- Databricks Workspace
- Terraform Installed
- Power BI for reporting

## How to Use

1. Clone this repository.
2. Follow the Terraform setup instructions.
3. Use Databricks to manage data transformations.
4. Access the Power BI report to view insights.

## Contact

For any questions, please contact [Your Name/Your Company].

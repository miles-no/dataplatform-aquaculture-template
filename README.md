# AquaCulte Data Platform

## Overview

This project is a template for a data platform designed for small and medium-large aquaculture companies in Norway. It leverages the power of Azure, Databricks, and Terraform to provide a scalable and efficient solution for managing and transforming data. The platform follows the **Medallion Architecture** and fetches data daily from [api.havvarsel.no](https://api.havvarsel.no).

## Architecture

- **Azure Databricks Architecture**: This platform is built on the Azure Databricks architecture, providing a unified analytics framework that integrates with Azure services. You can learn more about Azure Databricks architecture [here](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture).
  
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

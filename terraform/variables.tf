
variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "baeaf599-3dbd-4063-a939-8a4dca2de156"
}

variable "location" {
  description = "Location of the data center to host the Azure Resources"
  type        = string
  default     = "norwayeast"
}

variable "github_repo" {
  description = "The github repository where the code is stored"
  type        = string
  default     = "https://github.com/miles-no/dataplatform-aquaculture-template.git"
}

variable "container_image" {
  description = "Container Image Name"
  default     = "aquaapi:latest"
}

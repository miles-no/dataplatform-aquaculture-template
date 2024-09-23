
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

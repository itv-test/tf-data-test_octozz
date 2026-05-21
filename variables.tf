# variable "project_id" {
#   type        = string
#   description = "Project ID to deploy resources in."
# }

# variable "environment" {
#   description = "Environment of the deployed project."
#   type        = string
#   validation {
#     condition     = var.environment == "dev" || var.environment == "prd" || var.environment == "pre" || var.environment == "sbx"
#     error_message = "The environment must be one of 'dev', 'prd', 'pre', or 'sbx'."
#   }
# }

# variable "region" {
#   type        = string
#   description = "Region to deploy resources in"
#   default     = "europe-west2"
# }

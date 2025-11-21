variable "aws_region" {
    default = "ap-southeast-1"
}

variable "project_name" {
    default = "beBit-pretest"
}


variable "db_username" {
    description = "Database username"
    type        = string
}

variable "db_password" {
    description = "Database password"
    type = string
}

variable "db_name" {
    description = "Database name"
    type        = string
}

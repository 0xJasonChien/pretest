variable "project_name" {
    type = string
}

variable "db_endpoint" {
    type = string
}

variable "db_username" {
    type = string
}

variable "db_password" {
    type = string
}

variable "db_name" {
    type = string
}


variable "ecr_repository_url" {
    type = string
}

variable "vpc_id" {
    type = string
}

variable "private_subnets_ids" {
    type = list(string)
}

variable "public_subnets_ids" {
    type = list(string)
}

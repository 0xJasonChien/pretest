variable "aws_region" {
    default = "ap-northeast-1"
}

variable "project_name" {
    default = "beBit-pretest"
}

variable "docker_image" {
    description = "Docker image URI in ECR"
    type        = string
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

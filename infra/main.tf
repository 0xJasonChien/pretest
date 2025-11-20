terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 5.0"
        }
    }

    backend "s3" {
        bucket         = "jason-deployment-terraform-state"
        key            = "beBit/terraform.tfstate"
        region         = "ap-southeast-1"
        encrypt        = true
        use_lockfile = true
    }
}

provider "aws" {
    region = var.aws_region
}

module "vpc" {
    source = "./vpc"
}

module "ecs" {
    source = "./ecs"
    db_username  = var.db_username
    db_password  = var.db_password
    db_name      = var.db_name
    project_name = var.project_name
    docker_image = var.docker_image
}

module "rds" {
    source = "./rds"
    db_username  = var.db_username
    db_password  = var.db_password
    db_name      = var.db_name
    project_name = var.project_name
}

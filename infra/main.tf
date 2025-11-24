terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket       = "jason-deployment-terraform-state"
    key          = "beBit/terraform.tfstate"
    region       = "ap-southeast-1"
    encrypt      = true
    use_lockfile = true
  }
}

provider "aws" {
  region = "ap-southeast-1"
}

module "vpc" {
  source = "./vpc"
}

module "ecr" {
  source       = "./ecr"
  project_name = var.project_name
}

module "ecs" {
  source       = "./ecs"
  project_name = var.project_name

  db_username = var.db_username
  db_password = var.db_password
  db_name     = var.db_name
  db_endpoint = module.rds.endpoint

  ecr_repository_url = module.ecr.ecr_repository_url

  vpc_id              = module.vpc.vpc_id
  public_subnets_ids  = module.vpc.public_subnets_ids
  private_subnets_ids = module.vpc.private_subnets_ids
}

module "rds" {
  source       = "./rds"
  project_name = var.project_name

  db_username = var.db_username
  db_password = var.db_password
  db_name     = var.db_name
  private_subnet_ids = module.vpc.private_subnets_ids
}

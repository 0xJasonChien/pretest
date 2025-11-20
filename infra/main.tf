terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 5.0"
        }
    }

    backend "s3" {
        bucket         = "terraform-state"
        key            = "beBit/terraform.tfstate"
        region         = "ap-southeast-1"
        dynamodb_table = "terraform-lock"
        encrypt        = true
    }
}

provider "aws" {
    region = var.aws_region
}

# 載入 ECS 與 RDS 子模組
module "ecs" {
    source = "./ecs"
}

module "rds" {
    source = "./rds"
}


resource "aws_security_group" "rds_sg" {
    name        = "${var.project_name}-rds-sg"
    description = "Allow inbound access from ECS"
    vpc_id      = var.vpc_id

    # [關鍵] 允許 ECS SG 連進來
    ingress {
        protocol        = "tcp"
        from_port       = 5432
        to_port         = 5432
        security_groups = [var.ecs_security_group_id]
    }

    egress {
        protocol    = "-1"
        from_port   = 0
        to_port     = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_subnet_group" "default" {
    name       = "${var.project_name}-db-subnet-group"
    subnet_ids = var.private_subnet_ids
}

resource "aws_db_instance" "db" {
    identifier           = replace(lower(var.project_name), "_", "-")
    allocated_storage    = 20
    storage_type         = "gp2"
    engine               = "postgres"
    engine_version       = "18"
    instance_class       = "db.t4g.micro"
    db_name = var.db_name
    username             = var.db_username
    password             = var.db_password
    publicly_accessible  = false
    skip_final_snapshot  = true

    db_subnet_group_name = aws_db_subnet_group.default.name
}

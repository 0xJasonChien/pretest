resource "aws_db_instance" "db" {
    identifier           = var.project_name
    allocated_storage    = 20
    storage_type         = "gp2"
    engine               = "postgres"
    engine_version       = "14"
    instance_class       = "db.t4g.micro"
    username             = var.db_username
    password             = var.db_password
    publicly_accessible  = false
    skip_final_snapshot  = true
}

resource "aws_db_database" "project_db" {
    name     = var.db_name
    instance = aws_db_instance.db.id
}

output "endpoint" {
    value = aws_db_instance.db.endpoint
}

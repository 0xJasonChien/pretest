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
}

resource "aws_ecs_task_definition" "task_definition" {
    family                   = var.project_name
    requires_compatibilities = ["FARGATE"]
    network_mode             = "awsvpc"
    cpu                      = "512"
    memory                   = "1024"

    container_definitions = jsonencode([
        {
        name  = "backend"
        image = var.docker_image
        essential = true
        portMappings = [
            {
                containerPort = 8001
                hostPort      = 8001
            }
        ]
        environment = [
            {
            name  = "DB_HOST"
            value = module.rds.endpoint
            },
            {
            name  = "DB_PORT"
            value = "5432"
            },
            {
            name  = "DB_USER"
            value = var.db_username
            },
            {
            name  = "DB_PASSWORD"
            value = var.db_password
            },
            {
            name  = "DB_NAME"
            value = var.db_name
            }
        ]
        }
    ])
}

output "task_definition_arn" {
    value = aws_ecs_task_definition.django.arn
}

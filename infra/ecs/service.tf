resource "aws_security_group" "ecs_sg" {
    name        = "${var.project_name}-ecs-sg"
    description = "ECS security group"
    vpc_id      = module.vpc.vpc_id

    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_ecs_service" "backend" {
    name            = var.project_name
    cluster         = aws_ecs_cluster.cluster.id
    task_definition = aws_ecs_task_definition.task_definition.arn
    launch_type     = "FARGATE"
    desired_count   = 1

    network_configuration {
        subnets          = module.vpc.private_subnets
        security_groups  = [aws_security_group.ecs_sg.id]
        assign_public_ip = true
    }

    load_balancer {
        target_group_arn = aws_lb_target_group.tg.arn
        container_name   = "backend"
        container_port   = 8001
    }

    depends_on = [aws_lb_listener.http]
}

output "service_name" {
    value = aws_ecs_service.backend.name
}

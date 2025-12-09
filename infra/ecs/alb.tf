resource "aws_security_group" "alb_sg" {
    name        = "${var.project_name}-alb-sg"
    description = "Security Group for ALB"
    vpc_id      = var.vpc_id

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

resource "aws_lb" "lb" {
    name               = "${var.project_name}-alb"
    internal           = false
    load_balancer_type = "application"
    subnets            = var.public_subnets_ids
    security_groups    = [aws_security_group.alb_sg.id]
}

resource "aws_lb_target_group" "tg" {
    name     = "${var.project_name}-tg"
    port     = 8001
    protocol = "HTTP"
    vpc_id   = var.vpc_id
    target_type = "ip"

    health_check {
        path                = "/"
        protocol            = "HTTP"
        interval            = 30
        timeout             = 5
        healthy_threshold   = 2
        unhealthy_threshold = 2
    }
}

resource "aws_lb_listener" "http" {
    load_balancer_arn = aws_lb.lb.arn
    port              = 80
    protocol          = "HTTP"

    default_action {
        type             = "forward"
        target_group_arn = aws_lb_target_group.tg.arn
    }
}

output "alb_dns" {
    value = aws_lb.lb.dns_name
}

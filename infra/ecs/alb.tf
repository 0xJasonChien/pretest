resource "aws_lb" "lb" {
    name               = "${var.project_name}-alb"
    internal           = false
    load_balancer_type = "application"
    subnets            = module.vpc.public_subnets
}

resource "aws_lb_target_group" "tg" {
    name     = "${var.project_name}-tg"
    port     = 8001
    protocol = "HTTP"
    vpc_id   = module.vpc.vpc_id
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

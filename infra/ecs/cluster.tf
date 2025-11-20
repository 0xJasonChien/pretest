resource "aws_ecs_cluster" "cluster" {
    name = var.project_name
}

output "cluster_name" {
    value = aws_ecs_cluster.cluster.name
}

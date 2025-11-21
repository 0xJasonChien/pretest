output "ecs_cluster_name" {
  value = module.ecs.cluster_name
}

output "ecs_service_name" {
  value = module.ecs.service_name
}

output "alb_dns" {
  value = module.ecs.alb_dns
}

output "rds_endpoint" {
  value = module.rds.endpoint
}

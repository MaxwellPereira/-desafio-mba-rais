variable "aws_region" {
  default = "us-east-2"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMR"
}

variable "key_pair_name" {
  default = "exercicio-mba"
}

variable "airflow_subnet_id" {
  default = "subnet-997ee1d5"
}

variable "vpc_id" {
  default = "vpc-988352f3"
}

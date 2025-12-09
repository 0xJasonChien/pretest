
# VPC
resource "aws_vpc" "dev" {
    cidr_block = "10.0.0.0/16"
    tags = {
        Name = "dev-vpc"
    }
}

# Get all the az the region
data "aws_availability_zones" "available" {}


# Public Subnet
resource "aws_subnet" "public_1" {
    vpc_id                  = aws_vpc.dev.id
    cidr_block              = "10.0.1.0/24"
    map_public_ip_on_launch = true
    availability_zone       = data.aws_availability_zones.available.names[0]

    tags = {
        Name = "dev-public-subnet-1"
    }
}

resource "aws_subnet" "public_2" {
    vpc_id            = aws_vpc.dev.id
    cidr_block        = "10.0.2.0/24"
    map_public_ip_on_launch = true
    availability_zone = data.aws_availability_zones.available.names[1]

    tags = {
        Name = "dev-public-subnet-2"
    }
}

# Private Subnet
resource "aws_subnet" "private_1" {
    vpc_id            = aws_vpc.dev.id
    cidr_block        = "10.0.3.0/24"
    availability_zone = data.aws_availability_zones.available.names[0]

    tags = {
        Name = "dev-private-subnet-1"
    }
}

resource "aws_subnet" "private_2" {
    vpc_id            = aws_vpc.dev.id
    cidr_block        = "10.0.4.0/24"
    availability_zone = data.aws_availability_zones.available.names[1]

    tags = {
        Name = "dev-private-subnet-2"
    }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.dev.id

    tags = {
        Name = "dev-igw"
    }
}


# Public Route Table
resource "aws_route_table" "public" {
    vpc_id = aws_vpc.dev.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw.id
    }

    tags = {
        Name = "dev-public-rt"
    }
}



resource "aws_route_table_association" "public_1_assoc" {
    subnet_id      = aws_subnet.public_1.id
    route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public_2_assoc" {
    subnet_id      = aws_subnet.public_2.id
    route_table_id = aws_route_table.public.id
}

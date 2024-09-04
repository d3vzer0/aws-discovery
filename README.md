# WIP: AWS-Discovery

AWS-Discovery is a tool designed to visualize AWS resources as nodes and edges within a Neo4J graph database. Inspired by BloodHound's approach for Active Directory, this tool helps in understanding and analyzing the relationships and dependencies between various AWS resources. Currently the tool directly indexes the nodes/edges via the Neo4J API, the plan is to integrate this via BloodHound later as well :) 

## Features

- **Resource Mapping**: Automatically discovers and maps AWS resources such as EC2 instances, S3 buckets, IAM roles, and more.
- **Graph Visualization**: Visualizes the relationships between AWS resources in a Neo4J graph database.
- **Customizable**: Easily extendable to include additional AWS services and custom resource types.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/d3vzer0/aws-discovery.git
    cd aws-discovery
    ```
2. ** TODO ** 

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Inspired by BloodHound;


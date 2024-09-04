from src.loader import AWSLoader
from jinja2 import Template
import typer

app = typer.Typer()


@app.command()
def nodegen(config_path: str, template_path: str = './cli/templates/awsnodes.py.j2'):
    """ Only used for development, generates a dynamic model template based on the AWS Config json

    Args:
        config_path (str): Path to AWS config dump
        template_path (str, optional): Path to aws node template. Defaults to './cli/templates/awsnodes.py.j2'.
    """
    aws_resources = AWSLoader.node_models(config_path)
    unique_types = {}

    typer.echo("Generating dynamic node models for AWS resources")
    for resource in aws_resources:
        if resource.resource_type not in unique_types:
            unique_types[resource.resource_type] = {}
        for relationship in resource.relationships:
            unique_types[resource.resource_type][relationship.resource_type] = relationship.relationship_type

    with open(template_path, 'r') as template_file:
        template_object = Template(template_file.read())
        template_rendered = template_object.render(resources=unique_types)

    typer.echo(template_rendered)

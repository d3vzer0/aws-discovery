from neo4j import GraphDatabase
from src.loader import AWSLoader
import typer
import os

app = typer.Typer()


@app.command()
def constraints() -> None:
    """Create neo4j constraints, ie. making AWS resource ID unique/primary
    """
    aws_resources = AWSLoader.node_classess()
    # Have to redo this bit later
    driver = GraphDatabase.driver(os.getenv('NEO_URI', 'bolt://localhost:7687'),
                                  auth=(os.getenv('NEO_USER', 'neo4j'), os.getenv('NEO_PASS')))

    typer.echo("Creating neo4j constraints for AWS resource id for all node types")
    for property, config in aws_resources.items():
        query = f'CREATE CONSTRAINT FOR (n:{config.__name__}) REQUIRE n.external_id IS UNIQUE'
        with driver.session(database='awsdiscovery') as session:
            session.run(query)
    typer.echo("Finished creating constraints!")


@app.command()
def from_file(config_path: str) -> None:
    """Imports AWS nodes/edges based on AWS config export

    Args:
        config_path (str): Path to AWS config export
    """
    aws_resources = AWSLoader.from_config_file(config_path)

    typer.echo("Started import of AWS resource nodes")
    for resource in aws_resources.resources:
        resource.save()

    typer.echo("Started creating relationships between AWS resource nodes")
    for resource in aws_resources.resources:
        resource.connect(node_classess=AWSLoader.node_classess())

    typer.echo("Done!")

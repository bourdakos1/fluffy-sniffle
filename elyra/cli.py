import click

from .pipeline.cli import pipeline
from .metadata.cli import metadata


@click.group()
def cli():
    pass


cli.add_command(pipeline)
cli.add_command(metadata)

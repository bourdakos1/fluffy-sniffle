import click


@click.group()
def metadata():
    pass


@click.command()
def random():
    click.echo("random")


metadata.add_command(random)

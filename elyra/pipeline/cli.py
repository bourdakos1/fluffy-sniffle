import click


@click.group()
def pipeline():
    pass


@click.command()
def submit():
    click.echo("submiting")


@click.command()
def run():
    click.echo("running")


pipeline.add_command(submit)
pipeline.add_command(run)

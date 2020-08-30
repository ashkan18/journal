import click

@click.command()
def version():
  click.echo("0.0.2")

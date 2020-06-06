import click

@click.command()
def version():
  #print_green(VERSION)
  click.echo("0.0.1")

import click

from journal.commands.version import version

@click.group
def cli():
  pass

cli.add_command(version)

if __name__ == '__main__':
  cli()
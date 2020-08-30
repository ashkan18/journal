import click

from journalists.commands.version import version
from journalists.commands.append import append
from journalists.commands.end import end

import click

@click.group()
def cli():
    pass

cli.add_command(version)
cli.add_command(append)
cli.add_command(end)

if __name__ == '__main__':
    cli()
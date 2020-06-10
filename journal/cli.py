import click

from journal.commands.version import version
from journal.commands.append import append
from journal.commands.end import end

import click

@click.group()
def cli():
    pass

cli.add_command(version)
cli.add_command(append)
cli.add_command(end)

if __name__ == '__main__':
    cli()
import os
import sys
import click

import work
import work.commands

__version__ = 'dev'
__architecture__ = 'dev'


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Log a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Log a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        cmd_folder = os.path.dirname(work.commands.__file__)
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and not filename.startswith('__init__'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        if sys.version_info[0] == 2:
            name = name.encode('ascii', 'replace')
        name = self._get_full_command_name(name)
        mod = __import__('work.commands.' + name,
                         None, None, ['cli'])
        return mod.cli

    @staticmethod
    def _get_full_command_name(partial_name):
        if partial_name not in work.commands.cmds:
            for cmd in work.commands.cmds:
                if cmd.startswith(partial_name):
                    return cmd
        return partial_name


@click.command(cls=ComplexCLI, context_settings={})
def cli():
    """A cli for creating and deploying labs projects."""
    pass


if __name__ == '__main__':
    cli()

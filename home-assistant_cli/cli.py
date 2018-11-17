"""Configuration plugin for Home Assistant CLI (hass-cli)."""
import os
import sys

import click

from homeassistant_cli.const import PACKAGE_NAME, __version__

CONTEXT_SETTINGS = dict(auto_envvar_prefix='HOMEASSISTANT')

pass_context = click.make_pass_decorator(Configuration, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'plugins'))


class HomeAssistantCli(click.MultiCommand):
    """The Home Assistant Command-line."""

    def list_commands(self, ctx):
        """List all command available as plugin."""
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and not filename.startswith('__'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Import the commands of the plugins."""
        try:
            mod = __import__('{}.plugins.{}'.format(PACKAGE_NAME, name),
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=HomeAssistantCli, context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
@click.option('--server', '-s',
              help='The URL of Home Assistant instance.', default="http://localhost:8123", show_defaults=True)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose, server):
    """A command line interface for Home Assistant."""
    import requests

    ctx.verbose = verbose
    ctx.server = server
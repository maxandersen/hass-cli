"""Location plugin for Home Assistant CLI (hass-cli)."""
import webbrowser
import urllib.parse

import click

from homeassistant_cli.cli import pass_context
from homeassistant_cli.helper import req, req_raw, format_output

@click.group('toggle')
@pass_context
def cli(ctx):
    """toggle data from Home Assistant"""

@cli.command()
@click.argument('entities', nargs=-1, required=True)
@pass_context
def state(ctx, entities):
    """toggle state from Home Assistant"""
    for entity in entities:
        res = req(ctx, "get", "states/{}".format(entity))
        
        state = res["state"]
        flip = {
            "on" : "off",
            "off": "on",
            "true": "false",
            "false": "true"
            }

        if state in flip:
            newstate = flip[state]
            click.echo("Toggling from {} to {}".format(state,newstate))
            res["state"] = flip[state]
            import json
            response = req_raw(ctx,"post", "states/{}".format(entity), json.dumps(res))
       
        else:
            click.echo("Do not know how to toggle state `{}` for `{}`".format(state,entity))

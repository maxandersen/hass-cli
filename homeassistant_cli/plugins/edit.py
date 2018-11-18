"""Location plugin for Home Assistant CLI (hass-cli)."""
import webbrowser
import urllib.parse
import yaml
import click
import json as json_

from homeassistant_cli.cli import pass_context
from homeassistant_cli.helper import req, req_raw, raw_format_output, format_output

@click.group('edit')
@pass_context
def cli(ctx):
    """Edit entities"""

@cli.command()
@click.argument('entity', required="true")
@click.option('--json')
@pass_context
def state(ctx, entity, json):
    """edit state from Home Assistant"""
    if json:
        response = req_raw(ctx,"post", "states/{}".format(entity), json)
    else:
        existing = req_raw(ctx,"get", "states/{}".format(entity)).json()
        
        existing = raw_format_output(ctx.output, existing)
        new = click.edit(existing,extension=".{}".format(ctx.output))

        if new is not None:
            print("Updating '{}'".format(entity))
            if(ctx.output=="yaml"):
                new = json_.dumps(yaml.load(new))
            response = req_raw(ctx,"post", "states/{}".format(entity), new)
        else:
            print("No edits/changes.")

    


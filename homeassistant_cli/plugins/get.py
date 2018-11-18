"""Location plugin for Home Assistant CLI (hass-cli)."""
import webbrowser
import urllib.parse

import click

import os
import homeassistant_cli.const as const
from homeassistant_cli.cli import pass_context
from homeassistant_cli.helper import req, req_raw, format_output,debug_requests_on
from requests.exceptions import HTTPError

@click.group('get')
@pass_context
def cli(ctx):
    """list info from Home Assistant"""

def get_entities(ctx, args, incomplete):
    if not hasattr(ctx, 'server'):
        ctx.server = os.environ.get('HASS_SERVER', const.DEFAULT_SERVER)
    
    if not hasattr(ctx, 'token'):
        ctx.token = os.environ.get('HASS_TOKEN')

    if not hasattr(ctx, "timeout"):
        ctx.timeout = os.environ.get('HASS_TIMEOUT', const.DEFAULT_TIMEOUT)

    try:
        x = req(ctx, "get", "states")
    except HTTPError:
        x = None

    entities = []

    if x is not None:
        for entity in x:
            entities.append((entity["entity_id"], ''))

        return [c for c in entities if incomplete in c[0]]
    else:
        return entities


@cli.command()
@click.argument('entities', nargs=-1, autocompletion=get_entities)
@pass_context
def state(ctx, entities):
    """Get/read state from Home Assistant"""
    
    if not entities:
        r = req_raw(ctx, "get", "states")
        click.echo(format_output(ctx,r.json()))
    else:
        for entity in entities:
            click.echo(format_output(ctx,req(ctx, "get", "states/{}".format(entity))))


@cli.command()
@pass_context
def event(ctx):
    """list events from Home Assistant"""

    click.echo(format_output(ctx,req(ctx, "get", "events")))
    
@cli.command()
@pass_context
def service(ctx):
    """list services from Home Assistant"""

    click.echo(format_output(ctx,req(ctx, "get", "services")))

@cli.command()
@click.argument('entities', nargs=-1) ## do time from/to as human delta dates
@pass_context
def history(ctx, entities):
    """list history from Home Assistant"""

    if not entities:
        click.echo(format_output(ctx,req(ctx, "get", "history/period")))
    else:
        for entity in entities:
            click.echo(format_output(ctx,req(ctx, "get", "history/period?filter_entity_id={}".format(entity))))

           
           
@cli.command()
@pass_context
def error(ctx):
    """get errors from Home Assistant"""
    
    click.echo(req_raw(ctx, "get", "error_log").text)



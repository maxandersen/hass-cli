Home Assistant Command-line Interface (``hass-cli``)
====================================================

The Home Assistant Command-line interface (``hass-cli``) allows one to
work with a local or a remote `Home Assistant <https://home-assistant.io>`_
instance directly from the command-line.

Examples:

.. code:: bash
hass-cli 

.. code:: bash
Usage: hass-cli [OPTIONS] COMMAND [ARGS]...

  A command line interface for Home Assistant.

Options:
  --version                 Show the version and exit.
  -s, --server TEXT         The server URL of Home Assistant instance.
                            [default: http://localhost:8123]
  --token TEXT              The Bearer token for Home Assistant instance.
  --timeout INTEGER         Timeout for network operations.
  -o, --output [json|yaml]  Output format  [default: json]
  -v, --verbose             Enables verbose mode.
  --help                    Show this message and exit.

Commands:
  discover  Discovery for the local network.
  edit      list info from Home Assistant
  get       list info from Home Assistant
  info      Get basic info from Home Assistant using /api/discovery_info.
  raw       call raw api (advanced)
  toggle    toggle data from Home Assistant

Clone the git repository and 

.. code:: bash

    $ pip3 install --editable .

A hard requirement is that ``hass-cli`` needs to support Python 3.4 because
Home Assistant is able to run with Python 3.4.2.


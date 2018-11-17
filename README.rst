Home Assistant Command-line Interface (``hass-cli``)
====================================================

The Home Assistant Command-line interface (``hass-cli``) allows one to
work with a local or a remote `Home Assistant <https://home-assistant.io>`_
instance directly from the command-line.

.. code:: bash

   $ hass-cli
    Usage: hass-cli [OPTIONS] COMMAND [ARGS]...

      A command line interface for Home Assistant.

    Options:
      --version            Show the version and exit.
      -s, --server TEXT      The IP address of Home Assistant instance.
      -t, --token TEXT  The API password of Home Assistant instance.
      -v, --verbose        Enables verbose mode.
      --help               Show this message and exit.

    Commands:
      discovery  Discovery for the local network.
      info       Get configuration details.
      list       List various entries of an instance.
      notify     Send a notification with a given service.
      state      Get, set or remove the state of entity.
      status     Show the status of an instance.

This tool is in ALPHA stage or a so-called prototype.

Clone the git repository and 

.. code:: bash

    $ pip3 install --editable .

A hard requirement is that ``hass-cli`` needs to support Python 3.4 because
Home Assistant is able to run with Python 3.4.2.


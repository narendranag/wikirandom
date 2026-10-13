# src/wikirandom/console.py

import textwrap
import locale

import click
import requests

from . import __version__

# Get the locale
current_locale = locale.getlocale()  # e.g., ('en_US', 'UTF-8')

# Extract the language code
language_code = current_locale[0].split('_')[0]  # e.g., 'en'

# Construct the Wikipedia URL
API_URL = f"https://{language_code}.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)

def main():
    """The wikirandom CLI."""
    try:
        with requests.get(API_URL) as response:
            if(response.raise_for_status()):
                raise click.Exception(response.text)
            else:
                data = response.json()
                
                title = data["title"]
                extract = data["extract"]

                click.secho(title, fg="green")
                click.echo(textwrap.fill(extract))
    except requests.exceptions.RequestException as e:
        raise click.ClickException(str(e))
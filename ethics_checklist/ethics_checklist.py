import click
import os
from pathlib import Path

import xerox

from .parser import Checklist
from .formats import FORMATS, EXTENSIONS

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'checklist.yml'

CHECKLIST_FILE = Path(os.environ.get('ETHICS_CHECKLIST', DEFAULT_CHECKLIST))


@click.command()
@click.option('--checklist', '-i', default=None, type=click.Path(exists=True), help='Override checklist file.')
@click.option('--format', '-f', default=None, type=str, help='Output format. Default is "markdown". \
                                                        File extesion used if --output is passed.')
@click.option('--output', '-o', default=None, type=click.Path(), help='Output file path.')
@click.option('--clipboard', '-c', is_flag=True, default=False, help='Whether or not to output to clipboard.')
@click.option('--overwrite', '-w', is_flag=True, default=False, help='Overwrite output file if it exists. \
                                                                      Default is False.')
def main(checklist, format, output, clipboard, overwrite):
    # load checklist
    cl_path = Path(checklist) if checklist else DEFAULT_CHECKLIST
    cl = Checklist.read(cl_path)

    output = Path(output) if output else None

    # get format by file extesion
    if output:
        ext = output.suffix
        output_format = EXTENSIONS[ext]

    if not format:
        output_format = 'markdown'
    else:
        output_format = format

    template = FORMATS[output_format](cl)

    # write output or print to stdout
    if output:
        template.write(output, overwrite=overwrite)
    elif clipboard:
        xerox.copy(template.render())
    else:
        click.echo(template.render())


if __name__ == '__main__':
    main()

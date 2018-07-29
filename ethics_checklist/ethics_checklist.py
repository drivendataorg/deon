import click
import os
from pathlib import Path

from .parser import Checklist, Section
from .formats import FORMATS, EXTENSIONS

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'checklist.json'

CHECKLIST_FILE = Path(os.environ.get('ETHICS_CHECKLIST', DEFAULT_CHECKLIST))


@click.command()
@click.option('--checklist', default=None, type=click.Path(exists=True), help='Override checklist file.')
@click.option('--format', default=None, type=str, help='Output format. Default is "markdown". File extesion used if --output is passed.')
@click.option('--output', default=None, type=click.Path(), help='Output file path.')
@click.option('--clipboard', is_flag=True, default=False, help='Whether or not to output to clipboard.')
@click.option('--overwrite', is_flag=True, default=False, help='Overwrite output file if it exists. Default is False.')
def main(checklist, format, output, clipboard, overwrite):
    # load checklist
    cl_path = Path(checklist) if checklist else DEFAULT_CHECKLIST
    cl = Checklist.read(cl_path)

    output = Path(output) if output else None

    # get format by file extesion
    if output:
        ext = output.suffix
        format = EXTENSIONS[ext]

    if not format:
        format = 'markdown'

    template = FORMATS[format](cl)

    # write output or print to stdout
    if output:
        template.write(output, overwrite=overwrite)
    elif clipboard:
        raise NotImplementedError("Output to clipboard NYI.")
    else:
        click.echo(template.render())


if __name__ == '__main__':
    main()




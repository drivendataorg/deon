import click
import os
from pathlib import Path

import xerox

from .parser import Checklist
from .formats import FORMATS, EXTENSIONS

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'checklist.yml'

CHECKLIST_FILE = Path(os.environ.get('ETHICS_CHECKLIST', DEFAULT_CHECKLIST))


@click.command()
@click.option('--checklist', '-l', default=None, type=click.Path(exists=True), help='Override checklist file.')
@click.option('--format', '-f', default=None, type=str,
              help='Output format. Default is "markdown". ' +
                   'Can be one of [{}]. '.format(', '.join(EXTENSIONS.values())) +
                   'File extension used if --output is passed.')
@click.option('--output', '-o', default=None, type=click.Path(),
              help='Output file path. Extension can be one of [{}]'.format(', '.join(EXTENSIONS.keys())))
@click.option('--clipboard', '-c', is_flag=True, default=False, help='Whether or not to output to clipboard.')
@click.option('--overwrite', '-w', is_flag=True, default=False, help='Overwrite output file if it exists. \
                                                                      Default is False.')
def main(checklist, format, output, clipboard, overwrite):
    # load checklist
    cl_path = Path(checklist) if checklist else DEFAULT_CHECKLIST
    cl = Checklist.read(cl_path)

    output = Path(output) if output else None

    # output extension is given priority if differing format is included
    if output:
        # get format by file extension
        ext = output.suffix
        if ext in EXTENSIONS.keys():
            output_format = EXTENSIONS[ext]
        else:
            raise click.UsageError('Output requires a file name with a supported extension.')
    elif format:
        if format in FORMATS:
            output_format = format
        else:
            raise click.UsageError('File format is not supported.')
    else:
        output_format = 'markdown'

    template = FORMATS[output_format](cl)

    # write output or print to stdout
    if output:
        template.write(output, overwrite=overwrite)
    elif clipboard:
        xerox.copy(str(template.render()))
    else:
        click.echo(template.render())


if __name__ == '__main__':
    main()

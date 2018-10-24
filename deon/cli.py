import click

from .deon import ExtensionException, FormatException, create

from .formats import EXTENSIONS


@click.command('deon')
@click.option('--checklist', '-l', default=None, type=click.Path(exists=True),
              help='Override default checklist file with a path to a custom checklist.yml file.')
@click.option('--format', '-f', 'output_format', default=None, type=str,
              help='Output format. Default is "markdown". ' +
                   'Can be one of [{}]. '.format(', '.join(EXTENSIONS.values())) +
                   'Ignored and file extension used if --output is passed.')
@click.option('--output', '-o', default=None, type=click.Path(),
              help='Output file path. Extension can be one of [{}] '.format(', '.join(EXTENSIONS.keys())) +
                   'The checklist is appended if the file exists.')
@click.option('--clipboard', '-c', is_flag=True, default=False,
              help='Whether or not to copy the output to the clipboard.')
@click.option('--overwrite', '-w', is_flag=True, default=False, help='Overwrite output file if it exists. \
                                                                      Default is False , which will append \
                                                                      to existing file.')
def main(checklist, output_format, output, clipboard, overwrite):
    try:
        result = create(checklist, output_format, output, clipboard, overwrite)
    except ExtensionException:
        with click.get_current_context() as ctx:
                msg = 'Output requires a file name with a supported extension.\n\n'
                raise click.ClickException(msg + ctx.get_help())
    except FormatException:
        with click.get_current_context() as ctx:
                msg = f"File format {output_format} is not supported.\n\n"
                raise click.ClickException(msg + ctx.get_help())
    else:
        # write output or print to stdout
        if result:
            click.echo(result)
        elif clipboard:
            click.echo("Checklist successfully copied to clipboard.")
        else:
            click.echo(f"Checklist successfully written to file {output}.")


if __name__ == '__main__':
    main()

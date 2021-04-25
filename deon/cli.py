import click
from pathlib import Path 
from .deon import ExtensionException, FormatException, MulticellException, create
import os

from .formats import EXTENSIONS


@click.command("deon")
@click.option(
    "--checklist",
    "-c",
    default=None,
    type=click.Path(exists=True),
    help="Override default checklist file with a path to a custom checklist.yml file.",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    default=None,
    type=str,
    help='Output format. Default is "markdown". '
    + "Can be one of [{}]. ".format(", ".join(EXTENSIONS.values()))
    + "Ignored and file extension used if --output is passed.",
)
@click.option(
    "--output",
    "-o",
    default=None,
    type=click.Path(),
    help="Output file path. Extension can be one of [{}]. ".format(", ".join(EXTENSIONS.keys()))
    + "The checklist is appended if the file exists.",
)
@click.option(
    "--overwrite",
    "-w",
    is_flag=True,
    default=False,
    help="Overwrite output file if it exists. "
    + "Default is False, which will append to existing file.",
)
@click.option(
    "--multicell",
    "-m",
    is_flag=True,
    default=False,
    help="For use with Jupyter format only. "
    + "Write checklist with multiple cells, one item per cell. "
    + "Default is False, which will write the checklist in a single cell.",
)
@click.option(
    "--toggleid",
    "-t",
    is_flag=True,
    default=False,
    help="Can toggle if IDs show",
)
@click.option(
    "--language",
    "-l",
    default=None,
    type=str,
    help="Changes the specified language",
)
@click.option(
    "--jobspecify",
    "-j",
    default=None,
    type=str,
    help="Changes the specified job",
)
def main(checklist, output_format, output, overwrite, multicell, toggleid, language, jobspecify):
    """Easily create an ethics checklist for your data science project.
    
    The checklist will be printed to standard output by default. Use the --output option to write
    to a file instead.
    """
    checklists = [checklist]
    outputs = [output]
    if checklist:
        if not str(checklist).lower().endswith('.yml'):
            checklists = []
            outputs = []
            for f in os.listdir(checklist):
                checklists.append(checklist + "/" + f)
                outputs.append(output + "/" + str(f).replace('.yml', '.html'))
            

    print(outputs, checklists)
    for value, cl in enumerate(checklists):
        try:
            result = create(cl, output_format, outputs[value], overwrite, multicell, toggleid, language, jobspecify)
        except ExtensionException:
            with click.get_current_context() as ctx:
                msg = "Output requires a file name with a supported extension.\n\n"
                raise click.ClickException(msg + ctx.get_help())
        except FormatException:
            with click.get_current_context() as ctx:
                msg = f"File format {output_format} is not supported.\n\n"
                raise click.ClickException(msg + ctx.get_help())
        except MulticellException:
            with click.get_current_context() as ctx:
                msg = f"Multicell is for use with jupyter format only. You used: {output_format}.\n\n"
                raise click.ClickException(msg + ctx.get_help())
        else:
            # write output or print to stdout
            if result:
                click.echo(result)
            else:
                click.echo(f"Checklist successfully written to file {output}.")


if __name__ == "__main__":
    main()

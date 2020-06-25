from pathlib import Path

import click
from click.testing import CliRunner
from jinja2 import Environment, FileSystemLoader
import yaml

from deon.cli import main as deon_command
from deon.formats import Markdown, EXTENSIONS
from deon.parser import Checklist


env = Environment(loader=FileSystemLoader("md_templates"),)

TEMPLATE_AND_OUTPUT = {
    "index.tpl": Path("docs/index.md"),
    "examples.tpl": Path("docs/examples.md"),
    "readme.tpl": Path("../README.md"),
}


def create_context():
    cl = Checklist.read(Path(__file__).absolute().parents[1] / "deon" / "assets" / "checklist.yml")
    checklist_template = Markdown(cl)
    rendered_checklist = checklist_template.render()

    runner = CliRunner()
    result = runner.invoke(deon_command, ["--help"])

    table = make_table_of_links()

    return {
        "default_checklist": rendered_checklist,
        "cli_options": result.output,
        "supported_formats": EXTENSIONS,
        "links_table": table,
    }


def make_table_of_links():
    """
    Generates table where lefthand column contains checklist items (from checklist.yml) and righthand column contains
    hyperlinks to examples where things have gone wrong (from examples.yml). Table appears in docs/docs/examples.md.
    """
    root = Path(__file__).absolute().parents[1] / "deon" / "assets"

    cl = Checklist.read(root / "checklist.yml")

    with open(root / "examples_of_ethical_issues.yml", "r") as f:
        refs = yaml.load(f, Loader=yaml.SafeLoader)

    refs_dict = dict()
    for r in refs:
        refs_dict[r["line_id"]] = r["links"]

    template = """<center>Checklist Question</center> | <center>Examples of Ethical Issues</center>
--- | ---
{lines}
"""
    line_template = "**{line_id} {line_summary}**: {line} | {row_text}"
    section_title_template = " | <center>**{section_title}**</center>"
    line_delimiter = "\n"

    formatted_rows = []
    for s in cl.sections:
        # section title row
        row = section_title_template.format(section_title=s.title)
        formatted_rows.append(row)

        for line in s.lines:
            # create bulleted list of links for each checklist item in that section
            bulleted_list = []
            for link in refs_dict[line.line_id]:
                text = link["text"]
                url = link["url"]
                bullet_hyperlink = f"<li>[{text}]({url})</li>"
                bulleted_list.append(bullet_hyperlink)
            formatted_bullets = "".join(bulleted_list)

            row = line_template.format(
                line_id=line.line_id,
                line_summary=line.line_summary,
                line=line.line,
                row_text=f"<ul>{formatted_bullets}</ul>",
            )
            formatted_rows.append(row)

    # bring all the rows together
    all_rows = line_delimiter.join(formatted_rows)
    return template.format(lines=all_rows)


@click.command()
def main():
    ctx = create_context()

    for t, o in TEMPLATE_AND_OUTPUT.items():
        tmpl = env.get_template(t)

        with open(o, "w", encoding="utf-8") as f:
            (tmpl.stream(**ctx).dump(f))


if __name__ == "__main__":
    main()

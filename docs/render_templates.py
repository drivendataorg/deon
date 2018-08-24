from pathlib import Path

import click
from click.testing import CliRunner
from jinja2 import Environment, FileSystemLoader
import yaml

from deon.ethics_checklist import main as deon_command
from deon.formats import Markdown, EXTENSIONS
from deon.parser import Checklist


env = Environment(
    loader=FileSystemLoader('md_templates'),
)

TEMPLATE_AND_OUTPUT = {
    'index.tpl': Path('docs/index.md'),
    'references.tpl': Path('docs/references.md'),
    'readme.tpl': Path('../README.md'),
}


def create_context():
    cl = Checklist.read(Path(__file__).absolute().parents[1] / 'checklist.yml')
    checklist_template = Markdown(cl)
    rendered_checklist = checklist_template.render()

    runner = CliRunner()
    result = runner.invoke(deon_command, ['--help'])

    table = make_table_of_links()

    return {
        'default_checklist': rendered_checklist,
        'cli_options': result.output,
        'supported_formats': EXTENSIONS,
        'links_table': table,
    }

def make_table_of_links():
    root = Path(__file__).absolute().parents[1]
    cl = Checklist.read(root / 'checklist.yml')

    # create dictionary of line ids and checklist questions
    question_dict = dict()
    for s in cl.sections:
        for l in s.lines:
            question_dict[l.line_id] = l.line

    section_dict = dict()
    for s in cl.sections:
        section_dict[s.section_id] = s.title

    with open(root / 'references.yml', 'r') as f:
        refs = yaml.load(f)

    template = """<center>Checklist Question</center> | <center>Examples of Ethical Issues</center>
--- | ---
{lines}
"""
    line_template = "{line_id} | {row_text}"
    line_delimiter = "\n"

    formatted_rows = []
    for checklist_item in refs:

        line_id = checklist_item['line_id']
        question = question_dict[line_id]

        # if have first item of a section, first include section title
        if line_id.split('.')[1] == '1':
            # break
            section_title = section_dict[line_id.split('.')[0]]
            row = line_template.format(line_id='',
                                       row_text=f"<center>**{section_title}**</center>")
            formatted_rows.append(row)

        bulleted_list = []
        for i, link in enumerate(checklist_item['links']):
            text = link['text']
            url = link['url']
            bullet_hyperlink = f"<li>[{text}]({url})</li>"
            bulleted_list.append(bullet_hyperlink)
        formatted_bullets = ''.join(bulleted_list)

        row = (line_template.format(
                line_id=f"**{line_id}**. {question}",
                row_text=f"<ul>{formatted_bullets}</ul>"))
        formatted_rows.append(row)

    all_rows = line_delimiter.join(formatted_rows)
    return template.format(lines=all_rows)


@click.command()
def main():
    ctx = create_context()

    for t, o in TEMPLATE_AND_OUTPUT.items():
        tmpl = env.get_template(t)

        with open(o, 'w') as f:
            (tmpl.stream(**ctx)
                 .dump(f))


if __name__ == '__main__':
    main()

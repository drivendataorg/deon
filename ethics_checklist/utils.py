from pathlib import Path

import yaml

from .parser import Checklist


def make_table_of_links():
    root = Path(__file__).parents[1]
    cl = Checklist.read(root / 'checklist.yml')

    # create dictionary of line ids and checklist questions
    question_dict = dict()
    for s in cl.sections:
        for l in s.lines:
            question_dict[l.line_id] = l.line

    with open(root / 'references.yml', 'r') as f:
        refs = yaml.load(f)

    template = """ Checklist Question | Examples of Ethical Issues
--- | ---
{lines}
"""
    line_template = "{line_id} | {row_text}"
    line_delimiter = "\n"

    formatted_rows = []
    for checklist_item in refs:

        line_id = checklist_item['line_id']
        question = question_dict[line_id]

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


if __name__ == '__main__':
    make_table_of_links()

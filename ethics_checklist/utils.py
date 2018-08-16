from pathlib import Path

import yaml

# from parser import Checklist


def make_table_of_links():
    root = Path(__file__).parents[1]
    # cl = Checklist.read(root / 'checklist.yml')

    with open(root / 'references.yml', 'r') as f:
        refs = yaml.load(f)

    template = """Question | Link
--- | ---
{lines}
"""
    line_template = "{line_id} | {hyperlink}"
    line_delimiter = "\n"

    formatted_rows = []
    for checklist_item in refs:
        line_id = checklist_item['line_id']

        for i, link in enumerate(checklist_item['links']):
            text = link['text']
            url = link['url']

            row_id = '' if i != 0 else line_id
            row = (line_template.format(
                    line_id=row_id,
                    hyperlink=f"[{text}]({url})"))
            formatted_rows.append(row)

    all_rows = line_delimiter.join(formatted_rows)
    return template.format(lines=all_rows)


if __name__ == '__main__':
    make_table_of_links()

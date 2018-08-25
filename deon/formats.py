import json
from pathlib import Path

from bs4 import BeautifulSoup


# File types
class Format(object):
    """ Template for a specific file type; renders and
        writes out to file.

        For text formats, simply override the templates
        below. For other formats, override `render`
        and `write`.
    """
    template = "{title}\n\n{sections}"
    append_delimiter = "\n\n"

    section_template = "{title}\n{lines}"
    section_delimiter = "\n\n"

    line_template = "* {line}"
    line_delimiter = "\n"

    def __init__(self, checklist, include_ids=True):
        self.checklist = checklist
        self.include_ids = include_ids

    def render_line(self, line):
        if self.include_ids:
            return "{} {}".format(line.line_id, line.line)
        else:
            return line.line

    def render(self):
        """ Uses the checklist and templates to render
            all of the components for this format.
        """
        rendered_sections = []
        for section in self.checklist.sections:
            rendered_lines = self.line_delimiter.join(
                [self.line_template.format(line=self.render_line(l)) for l in section.lines]
            )

            rendered_section = self.section_template.format(
                title=(section.title if not self.include_ids
                       else "{}. {}".format(section.section_id, section.title)),
                lines=rendered_lines
            )

            rendered_sections.append(rendered_section)

        all_sections = self.section_delimiter.join(rendered_sections)

        return self.template.format(title=self.checklist.title, sections=all_sections)

    def write(self, filepath, overwrite=False):
        """ Renders template and writes to `filepath`.

            If `overwrite=True`, write over anything at
            `filepath`. Else, if the file exists append to
            the end of file.
        """
        filepath = Path(filepath)

        text = self.render()

        mode = 'w' if not filepath.exists() or overwrite else 'a'
        if mode == 'a':
            text = self.append_delimiter + text

        with open(filepath, mode) as f:
            f.write(text)


class Markdown(Format):
    """ Markdown template items
    """
    template = "# {title}\n\n{sections}\n\n"
    section_template = """## {title}
{lines}"""

    line_template = " - [ ] {line}"


class Rst(Format):
    """reStructuredText template items
    """
    template = "{title}\n============\n\n{sections}\n\n"
    section_template = """{title}\n---------\n\n{lines}"""
    line_template = "* [ ] {line}"


class JupyterNotebook(Markdown):
    """ Jupyter notebook template items
    """

    append_delimiter = {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["-----\n"]
    }

    def render(self):
        """ Creates a cell with rendered Markdown of the
            checklist.
        """
        text = super().render()
        return {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                l + "\n" for l in text.split("\n")
            ]
        }

    def write(self, filepath, overwrite=False):
        """ If notebook does not exist (or `overwrite=True`), create a blank
            notebook and add the checklist. Otherwise append a cell with a
            horizontal rule and another cell with the checklist.
        """
        filepath = Path(filepath)

        if filepath.exists() and not overwrite:
            with open(filepath, 'r') as f:
                nbdata = json.load(f)

            nbdata['cells'].append(self.append_delimiter)
        else:
            # if new notebook, needs these properties
            blank_jupyter_notebook = {
                'nbformat': 4,
                'nbformat_minor': 2,
                'metadata': {},
                'cells': []
            }
            nbdata = blank_jupyter_notebook

        cell = self.render()
        nbdata['cells'].append(cell)

        with open(filepath, "w") as f:
            json.dump(nbdata, f)


class Html(Format):
    template = """<h1>{title}</h1>
<br/> <br/>
{sections}
<br/> <br/>"""
    section_template = """<h2>{title}</h2>
<hr/>
<ul>
{lines}
</ul>"""

    section_delimiter = """
<br/><br/>
"""

    line_template = "<li><input type='checkbox'>{line}</input></li>"
    line_delimiter = "\n"

    doc_template = """<html>
<body>
{text}
</body>
</html>
"""

    def write(self, filepath, overwrite=False):
        """ If notebook does not exist (or `overwrite=True`), create a blank
            notebook and add the checklist. Otherwise append a cell with a
            horizontal rule and another cell with the checklist.
        """
        filepath = Path(filepath)

        if filepath.exists() and not overwrite:
            # insert at end of body
            checklist = self.render()

            with open(filepath, "r") as f:
                soup = BeautifulSoup(f, 'html.parser')

            # add checklist to end of body
            soup.body.append(BeautifulSoup(checklist, 'html.parser'))
        else:
            rendered_html = self.doc_template.format(text=self.render())
            soup = BeautifulSoup(rendered_html, 'html.parser')

        text = soup.prettify()

        with open(filepath, "w") as f:
            f.write(text)


FORMATS = {
    'markdown': Markdown,
    'rst': Rst,
    'jupyter': JupyterNotebook,
    'html': Html,
    'ascii': Format,
}

# keep all extensions lowercase
EXTENSIONS = {
    '.rmd': 'markdown',
    '.md': 'markdown',
    '.rst': 'rst',
    '.ipynb': 'jupyter',
    '.html': 'html',
    '.txt': 'ascii',
}

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

        `render` should return an object whose string
        representation is a fully valid document of
        that format.
    """

    template = "{title}\n\n{sections}\n\n{docs_link}"
    append_delimiter = "\n\n"

    section_template = "{title}\n{lines}"
    section_delimiter = "\n\n"

    line_template = "* {line_id} {line_summary}: {line}"
    line_delimiter = "\n"
    docs_link = "Data Science Ethics Checklist generated with deon (http://deon.drivendata.org)."
    badge = None

    def __init__(self, checklist):
        self.checklist = checklist

    def render(self):
        """ Uses the checklist and templates to render
            all of the components for this format.
        """
        rendered_sections = []
        for section in self.checklist.sections:
            rendered_lines = self.line_delimiter.join(
                [
                    self.line_template.format(
                        line_id=line.line_id, line_summary=line.line_summary, line=line.line
                    )
                    for line in section.lines
                ]
            )

            rendered_section = self.section_template.format(
                title=("{}. {}".format(section.section_id, section.title)), lines=rendered_lines
            )

            rendered_sections.append(rendered_section)

        all_sections = self.section_delimiter.join(rendered_sections)

        return self.template.format(
            title=self.checklist.title,
            sections=all_sections,
            docs_link=self.docs_link,
            badge=self.badge,
        )  # noqa: E501

    def write(self, filepath, overwrite=False):
        """ Renders template and writes to `filepath`.

            If `overwrite=True`, write over anything at
            `filepath`. Else, if the file exists append to
            the end of file.
        """
        filepath = Path(filepath)

        text = self.render()

        mode = "w" if not filepath.exists() or overwrite else "a"
        if mode == "a":
            text = self.append_delimiter + text

        with open(filepath, mode) as f:
            f.write(text)


class Markdown(Format):
    """ Markdown template items
    """

    template = "# {title}\n{badge}\n{sections}\n\n{docs_link}"
    section_template = """## {title}
{lines}"""

    line_template = " - [ ] **{line_id} {line_summary}**: {line}"
    docs_link = (
        "*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*"
    )
    badge = """
[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)
"""  # noqa: E501


class Rst(Format):
    """reStructuredText template items
    """

    template = "{title}\n============\n\n{badge}\n\n{sections}\n\n{docs_link}"
    section_template = """{title}\n---------\n\n{lines}"""
    line_template = "* [ ] **{line_id} {line_summary}**: {line}"
    docs_link = (
        "*Data Science Ethics Checklist generated with* `deon <http://deon.drivendata.org>`_."
    )
    badge = """.. image:: https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square
   :target: http://deon.drivendata.org"""


class JsonDict(dict):
    """Suclass of dict with valid json string representation."""

    def __str__(self):
        return json.dumps(self)

    def __repr__(self):
        return json.dumps(self)


class JupyterNotebook(Markdown):
    """ Jupyter notebook template items
    """

    append_delimiter = {"cell_type": "markdown", "metadata": {}, "source": ["-----\n"]}

    def render(self):
        """ Creates json for a valid blank Jupyter notebook with a cell
            containing the rendered Markdown of the checklist.
        """
        text = super().render()

        checklist_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in text.split("\n")],
        }

        blank_jupyter_notebook = {
            "nbformat": 4,
            "nbformat_minor": 2,
            "metadata": {},
            "cells": [checklist_cell],
        }

        return JsonDict(blank_jupyter_notebook)

    def write(self, filepath, overwrite=False):
        """ If notebook does not exist (or `overwrite=True`), write new
            notebook with checklist. Otherwise append a cell with a
            horizontal rule and another cell with the checklist.
        """
        nbdata = self.render()

        filepath = Path(filepath)

        if filepath.exists() and not overwrite:
            with open(filepath, "r") as f:
                existing_nbdata = json.load(f)
            # Append cells into existing notebook's cells array
            existing_nbdata["cells"].append(self.append_delimiter)
            existing_nbdata["cells"].extend(nbdata["cells"])
            nbdata = existing_nbdata

        with open(filepath, "w") as f:
            json.dump(nbdata, f)


class JupyterNotebookMulticell(JupyterNotebook):
    """ Jupyter notebook multiple cell format
    """

    def render(self):
        text = super(JupyterNotebook, self).render()
        checklist_cells = [
            {"cell_type": "markdown", "metadata": {}, "source": [line]}
            for line in text.split("\n")
            if line != ""
        ]

        blank_jupyter_notebook = {
            "nbformat": 4,
            "nbformat_minor": 2,
            "metadata": {},
            "cells": checklist_cells,
        }

        return JsonDict(blank_jupyter_notebook)


class Html(Format):
    """HTML template items"""

    template = """<h1>{title}</h1>
<br/> <br/>
{badge}
<br/> <br/>
{sections}
<br/> <br/>
<em>Data Science Ethics Checklist generated with <a href="http://deon.drivendata.org">deon.</a></em>"""
    section_template = """<h2>{title}</h2>
<hr/>
<ul>
{lines}
</ul>"""

    section_delimiter = """
<br/>
"""

    line_template = (
        "<li><input type='checkbox'><strong>{line_id} {line_summary}:</strong> {line}</input></li>"
    )
    line_delimiter = "\n"
    badge = """
<a href="http://deon.drivendata.org/">
    <img
        src="https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square"
        alt="Deon badge"
    />
</a>
    """
    doc_template = """<html>
<body>
{text}
</body>
</html>
"""

    def render(self):
        """ Create a new blank HTML document with checklist as the body.
            Returned as a BeautifulSoup object.
        """
        rendered_html = self.doc_template.format(text=super().render())
        soup = BeautifulSoup(rendered_html, "html.parser")
        # string representation of soup is the raw html, so we can return it
        return soup

    def write(self, filepath, overwrite=False):
        """ If html document does not exist (or `overwrite=True`), write new
            html file with checklist. Otherwise append checklist to the end of
            the body of the existing html file.
        """
        filepath = Path(filepath)

        soup = self.render()

        if filepath.exists() and not overwrite:
            with open(filepath, "r") as f:
                existing_soup = BeautifulSoup(f, "html.parser")

            # add checklist to end of body
            existing_soup.body.contents.extend(soup.body.contents)
            soup = existing_soup

        text = soup.prettify()

        with open(filepath, "w") as f:
            f.write(text)


FORMATS = {
    "ascii": Format,
    "html": Html,
    "jupyter": JupyterNotebook,
    "jupyter-multicell": JupyterNotebookMulticell,
    "markdown": Markdown,
    "rmarkdown": Markdown,
    "rst": Rst,
}

# keep all extensions lowercase
EXTENSIONS = {
    ".txt": "ascii",
    ".html": "html",
    ".ipynb": "jupyter",
    ".md": "markdown",
    ".rmd": "rmarkdown",
    ".rst": "rst",
}

import json
from pathlib import Path


# File types
class Format(object):
    """ Template for a specific file type; renders and
        writes out to file.

        For text formats, simply override the templates
        below. For other formats, override `render`
        and `write`.
    """
    template = "{title}: {sections}"
    section_template = "{title}: {lines}"
    section_delimiter = "\n\n"

    line_template = "* {line}"
    section_delimiter = "\n\n"
    
    def __init__(self, checklist):
        self.checklist = checklist

    def render(self):
        """ Uses the checklist and templates to render
            all of the components for this format.
        """
        rendered_sections = []
        for section in self.checklist.sections:
            rendered_lines = self.line_delimiter.join(
                [self.line_template.format(line=l) for l in section.lines]
            )

            rendered_section = self.section_template.format(
                title=section.title,
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

        with open(filepath, mode) as f:
            f.write(text)


class Markdown(Format):
    """ Markdown template items
    """
    template = "# {title}\n\n{sections}\n\n"
    section_template = """## {title}
------
{lines}"""
    
    section_delimiter = "\n\n"

    line_template = " - [ ] {line}"
    line_delimiter = "\n"


class JupyterNotebook(Markdown):
    """ Markdown template items
    """
    # if new notebook, needs these properties
    nb_file_base = {
        'nbformat': 4,
        'nbformat_minor': 2,
        'metadata': {},
        'cells': []
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

            nbdata['cells'].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": ["-----\n"]
            })
        else:
            nbdata = self.nb_file_base

        cell = self.render()
        nbdata['cells'].append(cell)

        with open(filepath, "w") as f:
            json.dump(nbdata, f)


FORMATS = {
    'markdown': Markdown,
    'jupyter': JupyterNotebook,
}

EXTENSIONS = {
    '.md': 'markdown',
    '.ipynb': 'jupyter',
}


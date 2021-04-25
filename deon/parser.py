import yaml


class Checklist(object):
    """Stores a checklist data parsed from a yaml file."""
    cl = None

    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    @classmethod
    def read(cls, filepath, ids):
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            cl = data

        title = data["title"]
        
        print(ids)
        sections = []
        for s in data["sections"]:
            if not ids:
                lines = [
                    Line(line["line_id"], line["line_summary"], line["line"]) for line in s["lines"]
                ]
                sections.append(Section(s["title"], s["section_id"], lines))
            else:
                lines = [
                    Line("", line["line_summary"], line["line"]) for line in s["lines"]
                ]
                sections.append(Section(s["title"], "", lines))
            
        return cls(title, sections)

    def readJSON(filepath):
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)

        return data

class Section(object):
    """Stores the sections of the checklist that are read in
    from a file.
    """

    def __init__(self, title, section_id, lines):
        self.title = title
        self.section_id = section_id
        self.lines = lines


class Line(object):
    """ Store information about a line in a section."""

    def __init__(self, line_id, line_summary, line):
        self.line_id = line_id
        self.line_summary = line_summary
        self.line = line

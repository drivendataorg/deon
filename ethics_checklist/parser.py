import yaml


class Checklist(object):
    """ Stores a checklist data parsed from a yaml file.
    """
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    @classmethod
    def read(cls, filepath):
        with open(filepath, "r") as f:
            data = yaml.load(f)

        title = data['title']
        sections = [Section(s['title'], s['lines']) for s in data['sections']]

        return cls(title, sections)


class Section(object):
    """ Stores the sections of the checklist that are read in
        from a file.
    """
    def __init__(self, title, lines):
        self.title = title
        self.lines = lines

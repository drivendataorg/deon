from ethics_checklist.parser import Checklist, Section


def test_checklist():
    c = Checklist.read('checklist.yml')
    assert c.title == 'Data Science Ethics Checklist'
    assert [s.title for s in c.sections] == ['Data Collection', 'Exploratory Analysis']
    lines = [s.lines for s in c.sections]
    assert lines[1][1] == 'Fields with PII are not used or displayed unless necessary for the analysis.'

import yaml

from ethics_checklist.parser import Checklist


def test_checklist():
    c = Checklist.read('checklist.yml')

    with open('checklist.yml', "r") as f:
        raw_parsed = yaml.load(f)

    assert c.title == raw_parsed['title']

    assert [s.title for s in c.sections][2] == raw_parsed['sections'][2]['title']
    assert [s.section_id for s in c.sections][2] == raw_parsed['sections'][2]['section_id']

    assert c.sections[1].lines[1].line == raw_parsed['sections'][1]['lines'][1]['line']
    assert c.sections[1].lines[1].line_id == raw_parsed['sections'][1]['lines'][1]['line_id']

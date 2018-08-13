from ethics_checklist.parser import Checklist


def test_checklist():
    c = Checklist.read('checklist.yml')
    assert c.title == 'Data Science Ethics Checklist'
    assert [s.title for s in c.sections][2] == 'Data Storage'
    lines = [s.lines for s in c.sections]
    assert lines[1][1] == 'Have we considered sources of bias that could be introduced during ' \
                          'data collection and survey design and taken steps to mitigate those?'

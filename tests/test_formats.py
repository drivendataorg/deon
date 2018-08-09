from pytest import fixture

from ethics_checklist.parser import Checklist, Section
from ethics_checklist.formats import Markdown


@fixture
def checklist():
    s1 = Section('Section 1', ['first', 'second'])
    s2 = Section('Section 2', ['third', 'fourth'])
    cl = Checklist('My Checklist', [s1, s2])
    return cl


def test_format():
    pass


def test_markdown(checklist, tmpdir):
    known_good = '# My Checklist\n\n## Section 1\n------\n - [ ] first\n - [ ] '\
                 'second\n\n## Section 2\n------\n - [ ] third\n - [ ] fourth\n\n'

    m = Markdown(checklist)
    assert m.render() == known_good

    temp_file_path = tmpdir.join('test.md')
    m.write(temp_file_path, overwrite=True)
    assert temp_file_path.read() == known_good


def test_jupyter():
    pass

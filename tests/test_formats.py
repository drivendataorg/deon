from pytest import fixture
import json

from ethics_checklist.parser import Checklist, Section
from ethics_checklist.formats import Markdown, JupyterNotebook, Html


@fixture
def checklist():
    s1 = Section('Section 1', ['first', 'second'])
    s2 = Section('Section 2', ['third', 'fourth'])
    cl = Checklist('My Checklist', [s1, s2])
    return cl


def test_format():
    # does this need to be tested separately from markdown?
    pass


def test_markdown(checklist, tmpdir):
    known_good = '# My Checklist\n\n## Section 1\n------\n - [ ] first\n - [ ] ' \
                 'second\n\n## Section 2\n------\n - [ ] third\n - [ ] fourth\n\n'

    m = Markdown(checklist)
    assert m.render() == known_good

    temp_file_path = tmpdir.join('test.md')
    m.write(temp_file_path, overwrite=True)
    assert temp_file_path.read() == known_good


def test_jupyter(checklist, tmpdir):
    known_good = ({'cell_type': 'markdown',
                  'metadata': {},
                   'source': ['# My Checklist\n',
                               '\n',
                               '## Section 1\n',
                              '------\n',
                              ' - [ ] first\n',
                              ' - [ ] second\n',
                              '\n',
                              '## Section 2\n',
                              '------\n',
                              ' - [ ] third\n',
                              ' - [ ] fourth\n',
                              '\n',
                              '\n']})

    j = JupyterNotebook(checklist)
    assert j.render() == known_good

    temp_file_path = tmpdir.join('test.ipynb')
    j.write(temp_file_path, overwrite=True)
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    assert nbdata['cells'] == [known_good]


def test_html(checklist, tmpdir):
    known_good = """<html>
<body>
<h1>My Checklist</h1>
<br/> <br/>
<h2>Section 1</h2>
<hr/>
<ul>
<li><input type='checkbox'>first</input></li>
<li><input type='checkbox'>second</input></li>
</ul>
<br/><br/>
<h2>Section 2</h2>
<hr/>
<ul>
<li><input type='checkbox'>third</input></li>
<li><input type='checkbox'>fourth</input></li>
</ul>
<br/> <br/>
</body>
</html>
"""
    h = Html(checklist)
    temp_file_path = tmpdir.join('test.html')
    h.write(temp_file_path, overwrite=True)
    with open(temp_file_path, 'r') as f:
        html_text = f.read()
    assert html_text == known_good

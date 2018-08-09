from pytest import fixture
import json

from ethics_checklist.parser import Checklist, Section
from ethics_checklist.formats import Format, Markdown, JupyterNotebook, Html


@fixture
def checklist():
    s1 = Section('Section 1', ['first', 'second'])
    s2 = Section('Section 2', ['third', 'fourth'])
    cl = Checklist('My Checklist', [s1, s2])
    return cl


# def test_format(checklist):
#     t = Format(checklist)
#     t.write('test.txt')
#     # assert t.render() == known_good


def test_markdown(checklist, tmpdir):
    known_good = '# My Checklist\n\n## Section 1\n------\n - [ ] first\n - [ ] ' \
                 'second\n\n## Section 2\n------\n - [ ] third\n - [ ] fourth\n\n'
    existing_text = 'There is existing text in this file.'

    m = Markdown(checklist)
    assert m.render() == known_good

    # no existing file
    temp_file_path = tmpdir.join('test.md')
    m.write(temp_file_path)
    assert temp_file_path.read() == known_good

    # append to existing file
    with open(temp_file_path, 'w') as f:
        f.write(existing_text)
    m.write(temp_file_path, overwrite=False)
    assert temp_file_path.read() == existing_text + known_good

    # overwrite existing file
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
  <h1>
   My Checklist
  </h1>
  <br/>
  <br/>
  <h2>
   Section 1
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    first
   </li>
   <li>
    <input type="checkbox"/>
    second
   </li>
  </ul>
  <br/>
  <br/>
  <h2>
   Section 2
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    third
   </li>
   <li>
    <input type="checkbox"/>
    fourth
   </li>
  </ul>
  <br/>
  <br/>
 </body>
</html>
"""
    existing_text = """<html>
<body>
There is existing text in this file.
</body>
</html>
"""
    inserted_known_good = """<html>
 <body>
  There is existing text in this file.
  <h1>
   My Checklist
  </h1>
  <br/>
  <br/>
  <h2>
   Section 1
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    first
   </li>
   <li>
    <input type="checkbox"/>
    second
   </li>
  </ul>
  <br/>
  <br/>
  <h2>
   Section 2
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    third
   </li>
   <li>
    <input type="checkbox"/>
    fourth
   </li>
  </ul>
  <br/>
  <br/>
 </body>
</html>
"""
    # no existing file
    h = Html(checklist)
    temp_file_path = tmpdir.join('test.html')
    h.write(temp_file_path)
    with open(temp_file_path, 'r') as tempf:
        assert tempf.read() == known_good

    # append to existing file
    with open(temp_file_path, 'w') as tempf:
        tempf.write(existing_text)
    h.write(temp_file_path, overwrite=False)
    with open(temp_file_path, 'r') as tempf:
        assert tempf.read() == inserted_known_good

    # overwrite existing file
    h.write(temp_file_path, overwrite=True)
    with open(temp_file_path, 'r') as tempf:
        assert tempf.read() == known_good

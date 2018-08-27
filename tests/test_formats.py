from pytest import fixture
import json

from deon.parser import Checklist, Section, Line
from deon.formats import Format, Markdown, JupyterNotebook, Html, Rst

import assets


@fixture
def checklist():
    s1 = Section('First section', 'A', [Line('A.1', 'A1sum', 'First A line'),
                                        Line('A.2', 'A2sum', 'Second A line')])
    s2 = Section('Second section', 'B', [Line('B.1', 'B1sum', 'First B line'),
                                         Line('B.2', 'B2sum', 'Second B line')])
    cl = Checklist('My Checklist', [s1, s2])
    return cl


def test_format(checklist, tmpdir):
    known_good = assets.known_good_ascii
    existing_text = assets.existing_text

    t = Format(checklist)

    # no existing file
    temp_file_path = tmpdir.join('test.txt')
    assert t.render() == known_good
    t.write(temp_file_path)
    assert temp_file_path.read() == known_good

    # append to existing file
    with open(temp_file_path, 'w') as f:
        f.write(existing_text)
    t.write(temp_file_path, overwrite=False)
    assert temp_file_path.read() == existing_text + Format.append_delimiter + known_good

    # overwrite existing file
    t.write(temp_file_path, overwrite=True)
    assert temp_file_path.read() == known_good


def test_markdown(checklist, tmpdir):
    known_good = assets.known_good_markdown
    existing_text = assets.existing_text

    m = Markdown(checklist)
    assert m.render() == known_good

    # no existing file
    temp_file_path = tmpdir.join('test.md')
    m.write(temp_file_path)
    assert temp_file_path.read() == known_good

    # Rmd also works
    temp_file_path = tmpdir.join('test.Rmd')
    m.write(temp_file_path)
    assert temp_file_path.read() == known_good

    # append to existing file
    with open(temp_file_path, 'w') as f:
        f.write(existing_text)
    m.write(temp_file_path, overwrite=False)
    assert temp_file_path.read() == existing_text + Markdown.append_delimiter + known_good

    # overwrite existing file
    m.write(temp_file_path, overwrite=True)
    assert temp_file_path.read() == known_good


def test_rst(checklist, tmpdir):
    known_good = assets.known_good_rst
    existing_text = assets.existing_text

    r = Rst(checklist)
    assert r.render() == known_good

    # no existing file
    temp_file_path = tmpdir.join('test.rst')
    r.write(temp_file_path)
    assert temp_file_path.read() == known_good

    # append to existing file
    with open(temp_file_path, 'w') as f:
        f.write(existing_text)
    r.write(temp_file_path, overwrite=False)
    assert temp_file_path.read() == existing_text + Rst.append_delimiter + known_good

    # overwrite existing file
    r.write(temp_file_path, overwrite=True)
    assert temp_file_path.read() == known_good


def test_jupyter(checklist, tmpdir):
    known_good = assets.known_good_jupyter

    j = JupyterNotebook(checklist)
    assert j.render() == known_good
    temp_file_path = tmpdir.join('test.ipynb')

    # no existing file
    j.write(temp_file_path)
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    assert nbdata['cells'] == [known_good]

    # append to existing file
    j.write(temp_file_path, overwrite=False)
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    assert len(nbdata['cells']) == 3
    assert nbdata['cells'][0] == known_good
    assert nbdata['cells'][1] == JupyterNotebook.append_delimiter
    assert nbdata['cells'][0] == nbdata['cells'][-1]

    # overwrite existing file
    j.write(temp_file_path, overwrite=True)
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    print(json.dumps(nbdata, indent=4))
    assert nbdata['cells'] == [known_good]


def test_html(checklist, tmpdir):
    known_good = assets.known_good_html
    existing_text = assets.existing_text_html
    inserted_known_good = assets.known_good_inserted_html
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

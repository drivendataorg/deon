from pytest import fixture
from click.testing import CliRunner

import yaml
import json

from ethics_checklist.ethics_checklist import main
from ethics_checklist import assets


@fixture
def checklist(tmpdir):
    temp_checklist = tmpdir.join('checklist.yml')
    with open(temp_checklist, 'w') as f:
        data = {'title': 'My Checklist',
                'sections': [
                    {'title': 'First section',
                     'section_id': 'A',
                     'lines': [
                        {'line_id': 'A.1',
                         'line': 'First A line'},
                        {'line_id': 'A.2',
                         'line': 'Second A line'}
                     ]},
                    {'title': 'Second section',
                     'section_id': 'B',
                     'lines': [
                        {'line_id': 'B.1',
                         'line': 'First B line'},
                        {'line_id': 'B.2',
                         'line': "Second B line"}
                     ]}
                ]}
        yaml.dump(data, f)
    return temp_checklist


def test_ethics_checklist_default_md(checklist, tmpdir):
    runner = CliRunner()
    temp_file_path = tmpdir.join('test.md')
    result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path])
    assert result.exit_code == 0
    assert temp_file_path.read() == assets.known_good_markdown


def test_ethics_checklist_ouptut_jupyter(checklist, tmpdir):
    runner = CliRunner()
    temp_file_path = tmpdir.join('test.ipynb')
    result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path])
    assert result.exit_code == 0
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    assert nbdata['cells'][0] == assets.known_good_jupyter


def test_ethics_checklist_format_jupyter(checklist, tmpdir):
    runner = CliRunner()
    temp_file_path = tmpdir.join('test.ipynb')
    result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path, '--format', 'jupyter'])
    assert result.exit_code == 0
    with open(temp_file_path, 'r') as f:
        nbdata = json.load(f)
    assert nbdata['cells'][0] == assets.known_good_jupyter

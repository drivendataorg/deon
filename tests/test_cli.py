from pytest import fixture
from click.testing import CliRunner

import yaml
import json
import xerox

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


@fixture
def test_dict():
    test_files_dict = {
        'markdown': ['test.md', assets.known_good_markdown],
        'html': ['test.html', assets.known_good_html],
        'rst': ['test.rst', assets.known_good_rst],
        'jupyter': ['test.ipynb', assets.known_good_jupyter]
    }
    return test_files_dict


def test_output(checklist, tmpdir, test_dict):
    runner = CliRunner()
    for k, v in test_dict.items():
        temp_file_path = tmpdir.join(v[0])
        result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path])
        assert result.exit_code == 0

        if k != 'jupyter':
            assert temp_file_path.read() == v[1]
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == v[1]

    unsupported_output = tmpdir.join('test.doc')
    result = runner.invoke(main, ['--checklist', checklist, '--output', unsupported_output])
    assert result.exit_code == 2
    assert "Error" in result.output

    temp_file_path = tmpdir.join('checklist.html')
    result = runner.invoke(main, ['--checklist', checklist, '-o', temp_file_path])
    assert temp_file_path.read() == assets.known_good_html


def test_format(checklist, tmpdir, test_dict):
    runner = CliRunner()
    for k, v in test_dict.items():
        result = runner.invoke(main, ['--checklist', checklist, '--format', k])
        assert result.exit_code == 0
        if k != 'html':  # full doc for html not returned with format
            # echo includes new line at end hence checking if known asset is in stdout
            assert str(v[1]) in result.output  # requires string for testing as jupyter known asset is a dict

    result = runner.invoke(main, ['--checklist', checklist, '--format', 'doc'])
    assert result.exit_code == 2
    assert "File format is not supported" in result.output

    result = runner.invoke(main, ['--checklist', checklist, '-f', 'rst'])
    assert assets.known_good_rst in result.output


def test_overwrite(checklist, tmpdir, test_dict):
    runner = CliRunner()
    for k, v in test_dict.items():
        temp_file_path = tmpdir.join(v[0])
        with open(temp_file_path, 'w') as f:
            f.write(assets.existing_text)
        result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path, '--overwrite'])
        assert result.exit_code == 0

        if k != 'jupyter':
            assert temp_file_path.read() == v[1]
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == v[1]

    temp_file_path = tmpdir.join('checklist.md')
    with open(temp_file_path, 'w') as f:
            f.write(assets.existing_text)
    result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path, '-w'])
    assert temp_file_path.read() == assets.known_good_markdown


def test_clipboard(checklist, tmpdir, test_dict):
    runner = CliRunner()
    for k, v in test_dict.items():
        result = runner.invoke(main, ['--checklist', checklist, '--clipboard', '--format', k])
        assert result.exit_code == 0
        if k != 'html':  # full doc for html not returned with format
            assert xerox.paste() == str(v[1])

    result = runner.invoke(main, ['--checklist', checklist, '-c'])
    assert result.exit_code == 0
    assert xerox.paste() == assets.known_good_markdown


def test_checklist(tmpdir, test_dict):
    abridged_checklist = tmpdir.join('abridged_checklist.yml')
    with open(abridged_checklist, 'w') as f:
        data = {'title': 'My Checklist',
                'sections': [
                    {'title': 'First section',
                     'section_id': 'A',
                     'lines': [
                        {'line_id': 'A.1',
                         'line': 'First A line'},
                        {'line_id': 'A.2',
                         'line': 'Second A line'}
                     ]}
                ]}
        yaml.dump(data, f)
    runner = CliRunner()
    result = runner.invoke(main, ['--checklist', abridged_checklist])
    assert result.exit_code == 0
    result = runner.invoke(main, ['-l', abridged_checklist])
    assert result.exit_code == 0


def test_default(checklist):
    runner = CliRunner()
    result = runner.invoke(main, ['--checklist', checklist])
    assert result.exit_code == 0
    assert assets.known_good_markdown in result.output


def test_multiple_options(checklist):
    runner = CliRunner()
    runner.invoke(main, ['--checklist', checklist, '-c', '-f', 'rst'])
    assert xerox.paste() == assets.known_good_rst

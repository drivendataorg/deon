import json

import xerox
import yaml
from click.testing import CliRunner

import assets
from deon.cli import main


def test_cli_output(checklist, tmpdir, test_format_configs):
    runner = CliRunner()
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path])
        print(result.output)
        assert result.exit_code == 0

        if frmt != 'jupyter':
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == known_good

    unsupported_output = tmpdir.join('test.doc')
    result = runner.invoke(main, ['--checklist', checklist, '--output', unsupported_output])
    assert result.exit_code == 1
    assert "Error" in result.output

    temp_file_path = tmpdir.join('checklist.html')
    result = runner.invoke(main, ['--checklist', checklist, '-o', temp_file_path])
    assert temp_file_path.read() == assets.known_good_html


def test_cli_format(checklist, tmpdir, test_format_configs):
    runner = CliRunner()
    for frmt, fpath, known_good in test_format_configs:
        result = runner.invoke(main, ['--checklist', checklist, '--format', frmt])
        assert result.exit_code == 0
        if frmt != 'html':  # full doc for html not returned with format
            # echo includes new line at end hence checking if known asset is in stdout
            assert str(known_good) in result.output  # requires string for testing as jupyter known asset is a dict

    result = runner.invoke(main, ['--checklist', checklist, '--format', 'doc'])
    assert result.exit_code == 1
    assert "File format is not supported" in result.output

    result = runner.invoke(main, ['--checklist', checklist, '-f', 'rst'])
    assert assets.known_good_rst in result.output


def test_cli_overwrite(checklist, tmpdir, test_format_configs):
    runner = CliRunner()
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        with open(temp_file_path, 'w') as f:
            f.write(assets.existing_text)
        result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path, '--overwrite'])
        assert result.exit_code == 0

        if frmt != 'jupyter':
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == known_good

    temp_file_path = tmpdir.join('checklist.md')
    with open(temp_file_path, 'w') as f:
            f.write(assets.existing_text)
    result = runner.invoke(main, ['--checklist', checklist, '--output', temp_file_path, '-w'])
    assert temp_file_path.read() == assets.known_good_markdown


def test_cli_clipboard(checklist, tmpdir, test_format_configs):
    runner = CliRunner()
    for frmt, fpath, known_good in test_format_configs:
        result = runner.invoke(main, ['--checklist', checklist, '--clipboard', '--format', frmt])
        assert result.exit_code == 0
        if frmt != 'html':  # full doc for html not returned with format
            assert xerox.paste() == str(known_good)

    result = runner.invoke(main, ['--checklist', checklist, '-c'])
    assert result.exit_code == 0
    assert xerox.paste() == assets.known_good_markdown


def test_checklist(tmpdir, test_format_configs):
    abridged_checklist = tmpdir.join('abridged_checklist.yml')
    with open(abridged_checklist, 'w') as f:
        data = {'title': 'My Checklist',
                'sections': [
                    {'title': 'First section',
                     'section_id': 'A',
                     'lines': [
                        {'line_id': 'A.1',
                         'line_summary': 'A1sum',
                         'line': 'First A line'},
                        {'line_id': 'A.2',
                         'line_summary': 'A2sum',
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
    runner.invoke(main, ['--checklist', checklist, '-c', '-f', 'ascii'])
    assert xerox.paste() == assets.known_good_ascii

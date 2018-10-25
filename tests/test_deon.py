import json

import pytest
import xerox

import deon
import assets


def test_output(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        deon.create(checklist, None, temp_file_path, False, False)

        if frmt != 'jupyter':
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == known_good

    unsupported_output = tmpdir.join('test.doc')
    with pytest.raises(deon.ExtensionException):
        deon.create(checklist, None, unsupported_output, False, False)


def test_format(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        result = deon.create(checklist, frmt, None, False, False)

        assert result is not None

        if frmt != 'html':  # full doc for html not returned with format
            # echo includes new line at end hence checking if known asset is in stdout
            assert known_good == result

    with pytest.raises(deon.FormatException):
        result = deon.create(checklist, 'doc', None, False, False)


def test_overwrite(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        with open(temp_file_path, 'w') as f:
            f.write(assets.existing_text)
        deon.create(checklist, None, temp_file_path, False, True)

        if frmt != 'jupyter':
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, 'r') as f:
                nbdata = json.load(f)
            assert nbdata['cells'][0] == known_good


def test_clipboard(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        deon.create(checklist, frmt, None, True, False)

        if frmt != 'html':  # full doc for html not returned with format
            assert xerox.paste() == str(known_good)

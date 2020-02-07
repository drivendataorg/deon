import json
from bs4 import BeautifulSoup

import pytest

import deon
import assets


def test_format(checklist, tmpdir, test_format_configs):
    for frmt, _, known_good in test_format_configs:
        result = str(
            deon.create(
                checklist, output_format=frmt, output=None, overwrite=False, multicell=False
            )
        )

        if frmt == "jupyter":
            # Jupyter requires json.dumps for double-quoting
            assert result == json.dumps(known_good)
            # Check that it's also valid json
            assert json.loads(result) == known_good
        elif frmt == "html":
            # Ensure valid html
            print(result)
            result_html = BeautifulSoup(result, "html.parser")
            known_good_html = BeautifulSoup(known_good, "html.parser")
            # Check html are equivalent ignoring formatting
            assert result_html.prettify() == known_good_html.prettify()
        else:
            assert result == str(known_good)


def test_multicell_success(checklist, tmpdir, test_format_configs):
    result = str(
        deon.create(
            checklist, output_format="jupyter", output=None, overwrite=False, multicell=True
        )
    )
    # Jupyter requires json.dumps for double-quoting
    assert result == json.dumps(assets.known_good_jupyter_multicell)
    # Check that it's also valid json
    assert json.loads(result) == assets.known_good_jupyter_multicell


def test_multicell_exception(checklist, tmpdir, test_format_configs):
    gen = (frmt for frmt, _, _ in test_format_configs if frmt != "jupyter")
    for frmt in gen:
        with pytest.raises(deon.deon.MulticellException):
            deon.create(
                checklist, output_format=frmt, output=None, overwrite=False, multicell=True
            )


def test_output(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        deon.create(
            checklist, output_format=None, output=temp_file_path, overwrite=False, multicell=False
        )

        if frmt != "jupyter":
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, "r") as f:
                nbdata = json.load(f)
            assert nbdata == known_good

    unsupported_output = tmpdir.join("test.doc")
    with pytest.raises(deon.ExtensionException):
        deon.create(
            checklist,
            output_format=None,
            output=unsupported_output,
            overwrite=False,
            multicell=False,
        )


def test_overwrite(checklist, tmpdir, test_format_configs):
    for frmt, fpath, known_good in test_format_configs:
        temp_file_path = tmpdir.join(fpath)
        with open(temp_file_path, "w") as f:
            f.write(assets.existing_text)
        deon.create(
            checklist, output_format=None, output=temp_file_path, overwrite=True, multicell=False
        )

        if frmt != "jupyter":
            assert temp_file_path.read() == known_good
        else:
            with open(temp_file_path, "r") as f:
                nbdata = json.load(f)
            assert nbdata == known_good

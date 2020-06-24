import pytest
import subprocess
import itertools as it
from click.testing import CliRunner

import assets
from deon.cli import main


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "arg, value, expected",
    [
        ("--format", ".doc", "Error: File format .doc is not supported."),
        ("--output", " checklist.doc", "Output requires a file name with a supported extension."),
    ],
)
def test_cli_errors(runner, arg, value, expected):
    result = runner.invoke(main, [arg, value])
    assert result.exit_code == 1
    assert expected in result.output


def test_cli_default(runner, checklist):
    result = runner.invoke(main, ["--checklist", checklist])
    assert result.exit_code == 0
    assert assets.known_good_markdown in result.output


@pytest.mark.parametrize("arg", ["--output", "-o"])
def test_cli_output(runner, checklist, tmpdir, test_format_configs, arg):
    temp_file_path = tmpdir.join("checklist.html")
    result = runner.invoke(main, ["--checklist", checklist, arg, temp_file_path])
    assert result.exit_code == 0
    assert temp_file_path.read() == assets.known_good_html


@pytest.mark.parametrize(
    "call,format",
    it.product(
        [["deon"], ["python", "-m", "deon"]],
        ["ascii", "html", "jupyter", "markdown", "rmarkdown", "rst"],
    ),
)
def test_base_call_no_error(call, format):
    status = subprocess.run(call + ["--format", format])
    assert status.returncode == 0

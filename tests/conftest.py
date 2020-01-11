import pytest
import yaml

import assets


@pytest.fixture
def checklist(tmpdir):
    temp_checklist = tmpdir.join("checklist.yml")
    with open(temp_checklist, "w") as f:
        data = {
            "title": "My Checklist",
            "sections": [
                {
                    "title": "First section",
                    "section_id": "A",
                    "lines": [
                        {"line_id": "A.1", "line_summary": "A1sum", "line": "First A line"},
                        {"line_id": "A.2", "line_summary": "A2sum", "line": "Second A line"},
                    ],
                },
                {
                    "title": "Second section",
                    "section_id": "B",
                    "lines": [
                        {"line_id": "B.1", "line_summary": "B1sum", "line": "First B line"},
                        {"line_id": "B.2", "line_summary": "B2sum", "line": "Second B line"},
                    ],
                },
            ],
        }
        yaml.dump(data, f)
    return temp_checklist


@pytest.fixture
def test_format_configs():
    test_format_config = [
        ("markdown", "test.md", assets.known_good_markdown),
        ("rmarkdown", "test.Rmd", assets.known_good_markdown),
        ("html", "test.html", assets.known_good_html),
        ("rst", "test.rst", assets.known_good_rst),
        ("jupyter", "test.ipynb", assets.known_good_jupyter),
        ("ascii", "test.txt", assets.known_good_ascii),
    ]
    return test_format_config

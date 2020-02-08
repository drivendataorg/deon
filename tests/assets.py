existing_text = "There is existing text in this file."

known_good_ascii = """My Checklist

A. First section
* A.1 A1sum: First A line
* A.2 A2sum: Second A line

B. Second section
* B.1 B1sum: First B line
* B.2 B2sum: Second B line

Data Science Ethics Checklist generated with deon (http://deon.drivendata.org)."""

known_good_markdown = """# My Checklist

[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)

## A. First section
 - [ ] **A.1 A1sum**: First A line
 - [ ] **A.2 A2sum**: Second A line

## B. Second section
 - [ ] **B.1 B1sum**: First B line
 - [ ] **B.2 B2sum**: Second B line

*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*"""  # noqa: E501

known_good_rst = """My Checklist
============

.. image:: https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square
   :target: http://deon.drivendata.org

A. First section
---------

* [ ] **A.1 A1sum**: First A line
* [ ] **A.2 A2sum**: Second A line

B. Second section
---------

* [ ] **B.1 B1sum**: First B line
* [ ] **B.2 B2sum**: Second B line

*Data Science Ethics Checklist generated with* `deon <http://deon.drivendata.org>`_."""

known_good_jupyter = {
    "nbformat": 4,
    "nbformat_minor": 2,
    "metadata": {},
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# My Checklist\n",
                "\n",
                "[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)\n",  # noqa: E501
                "\n",
                "## A. First section\n",
                " - [ ] **A.1 A1sum**: First A line\n",
                " - [ ] **A.2 A2sum**: Second A line\n",
                "\n",
                "## B. Second section\n",
                " - [ ] **B.1 B1sum**: First B line\n",
                " - [ ] **B.2 B2sum**: Second B line\n",
                "\n",
                "*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*"
                "\n",
            ],
        }
    ],
}

known_good_jupyter_multicell = {
    "nbformat": 4,
    "nbformat_minor": 2,
    "metadata": {},
    "cells": [
        {"cell_type": "markdown", "metadata": {}, "source": ["# My Checklist"]},
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)",  # noqa: E501
            ],
        },
        {"cell_type": "markdown", "metadata": {}, "source": ["## A. First section"]},
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [" - [ ] **A.1 A1sum**: First A line"],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [" - [ ] **A.2 A2sum**: Second A line"],
        },
        {"cell_type": "markdown", "metadata": {}, "source": ["## B. Second section"]},
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [" - [ ] **B.1 B1sum**: First B line"],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [" - [ ] **B.2 B2sum**: Second B line"],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*",
            ],
        },
    ],
}

known_good_html = """<html>
 <body>
  <h1>
   My Checklist
  </h1>
  <br/>
  <br/>
  <a href="http://deon.drivendata.org/">
   <img alt="Deon badge" src="https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square"/>
  </a>
  <br/>
  <br/>
  <h2>
   A. First section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    <strong>
     A.1 A1sum:
    </strong>
    First A line
   </li>
   <li>
    <input type="checkbox"/>
    <strong>
     A.2 A2sum:
    </strong>
    Second A line
   </li>
  </ul>
  <br/>
  <h2>
   B. Second section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    <strong>
     B.1 B1sum:
    </strong>
    First B line
   </li>
   <li>
    <input type="checkbox"/>
    <strong>
     B.2 B2sum:
    </strong>
    Second B line
   </li>
  </ul>
  <br/>
  <br/>
  <em>
   Data Science Ethics Checklist generated with
   <a href="http://deon.drivendata.org">
    deon.
   </a>
  </em>
 </body>
</html>
"""  # noqa: E501

existing_text_html = """<html>
<body>
There is existing text in this file.
</body>
</html>
"""

known_good_inserted_html = """<html>
 <body>
  There is existing text in this file.
  <h1>
   My Checklist
  </h1>
  <br/>
  <br/>
  <a href="http://deon.drivendata.org/">
   <img alt="Deon badge" src="https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square"/>
  </a>
  <br/>
  <br/>
  <h2>
   A. First section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    <strong>
     A.1 A1sum:
    </strong>
    First A line
   </li>
   <li>
    <input type="checkbox"/>
    <strong>
     A.2 A2sum:
    </strong>
    Second A line
   </li>
  </ul>
  <br/>
  <h2>
   B. Second section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    <strong>
     B.1 B1sum:
    </strong>
    First B line
   </li>
   <li>
    <input type="checkbox"/>
    <strong>
     B.2 B2sum:
    </strong>
    Second B line
   </li>
  </ul>
  <br/>
  <br/>
  <em>
   Data Science Ethics Checklist generated with
   <a href="http://deon.drivendata.org">
    deon.
   </a>
  </em>
 </body>
</html>
"""  # noqa: E501

existing_text = 'There is existing text in this file.'

known_good_ascii = """My Checklist

A. First section
* A.1 A1sum: First A line
* A.2 A2sum: Second A line

B. Second section
* B.1 B1sum: First B line
* B.2 B2sum: Second B line"""

known_good_markdown = """# My Checklist

## A. First section
 - [ ] A.1 A1sum: First A line
 - [ ] A.2 A2sum: Second A line

## B. Second section
 - [ ] B.1 B1sum: First B line
 - [ ] B.2 B2sum: Second B line

"""

known_good_rst = """My Checklist
============

A. First section
---------

* [ ] A.1 A1sum: First A line
* [ ] A.2 A2sum: Second A line

B. Second section
---------

* [ ] B.1 B1sum: First B line
* [ ] B.2 B2sum: Second B line

"""

known_good_jupyter = ({'cell_type': 'markdown',
                       'metadata': {},
                       'source': ['# My Checklist\n',
                                  '\n',
                                  '## A. First section\n',
                                  ' - [ ] A.1 A1sum: First A line\n',
                                  ' - [ ] A.2 A2sum: Second A line\n',
                                  '\n',
                                  '## B. Second section\n',
                                  ' - [ ] B.1 B1sum: First B line\n',
                                  ' - [ ] B.2 B2sum: Second B line\n',
                                  '\n',
                                  '\n']})

known_good_html = """<html>
 <body>
  <h1>
   My Checklist
  </h1>
  <br/>
  <br/>
  <h2>
   A. First section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    A.1 A1sum: First A line
   </li>
   <li>
    <input type="checkbox"/>
    A.2 A2sum: Second A line
   </li>
  </ul>
  <br/>
  <br/>
  <h2>
   B. Second section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    B.1 B1sum: First B line
   </li>
   <li>
    <input type="checkbox"/>
    B.2 B2sum: Second B line
   </li>
  </ul>
  <br/>
  <br/>
 </body>
</html>
"""

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
  <h2>
   A. First section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    A.1 A1sum: First A line
   </li>
   <li>
    <input type="checkbox"/>
    A.2 A2sum: Second A line
   </li>
  </ul>
  <br/>
  <br/>
  <h2>
   B. Second section
  </h2>
  <hr/>
  <ul>
   <li>
    <input type="checkbox"/>
    B.1 B1sum: First B line
   </li>
   <li>
    <input type="checkbox"/>
    B.2 B2sum: Second B line
   </li>
  </ul>
  <br/>
  <br/>
 </body>
</html>
"""

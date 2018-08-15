
# Using this package

The `ethics-checklist` is a command-line tool that allows you to easily add an ethics checklist to your data science projects. We support appending a checklist to existing analyses in [many formats](#Supported_file_types) or generating new files with a checklist that is ready to fill out or review. The checklist was inspired by an article published by O'Reilly: ["Checklists"]().

We recommend adding a checklist as the first step in your data science project. After creating your project folder, you could run:

```
$ethics-checklist -o ETHICS.md
```

This will create a markdown file that can be added to

For simple one-off analyses, you can append the checklist to a Jupyter notebook or RMarkdown file.

```
$jupyter notebook my-analysis.ipynb

...

$ethics-checklist -o my-analysis.ipynb  # appends cells to end of notebook
```

This checklist can be used by individuals or teams to ensure that reviewing the ethical implications of their work is part of every project. The checklist is meant as a jumping-off point, and it should spark deeper and more thourough discussions rather than replace those discussions.


# Supported file types

Here are the currently supported file types. We will accept pull requests with new file types if there is a strong case for widespread use of that filetype.

 - Markdown (including RMarkdown)
 - RST
 - Jupyter Notebooks
 - LaTeX
 - HTML
 - Rich Text (Can be used for Microsoft Word docs and Google Docs)


# Options

 - `-o / --ouptput [PATH]` - Output file to pass to; if not passed, the checklist is written to stdout.
 - `-c / --clipboard` - Send the checklist to the clipboard rather than to a file
 - `-f / --format [FORMAT]` - Useful with `--clipboard` since format is usually determined from the output file.
 - `-w / --overwrite` - Normally we append to an output file if it exists; if this flag is passed, we write a new file.
 - `-i / --checklist [PATH]` - If you want to override the built-in checklist with your own.

# Default Checklist

### Data collection

 - informed consent
 - anonymization
 - only collecting what you need

### Data storage
 - plans for data encryption
 - access controls
 - can a person request to be removed

### EDA
 - intellectual honesty in visualization, summary 
 - ensure data is fair in its representation

### Modeling
 - have we tested for fairness with respect to different user groups
 - have we built a model where we can explain results if we need to

### Deployment
 - can we turn it off
 - do we have a mechanism for redress
 - do we test for drift
 - have we thought about how it can be attacked?

# Changing the Checklist

This is not meant to be the only ethical checklist, but instead we try to capture reasonable defaults that are general enough to be widely useful. For your own projects with particular concerns, we recommend a fork of this repository for long-term maitence. An easy first pass is simply creating a new `checklist.ini` file, and using the `-i` flag.

Our goal is to have checklist items that are actionable as part of a review of data science work or as part of a plan. Please avoid suggesting items that are too vague (e.g., "do no harm") or too specific (e.g., "remove social security numbers from data"). 

Note: This process is an experiment and is subject to change based on how well it works. Our goal is to avoid :flame: wars in the issue threads while still making a tool that will make adding an ethics checklist to a project easy.

To request a change, please file an issue with a title that starts with one of: "CREATE, UPDATE, DELETE". There are FOUR requirements for an issue requesting a change to the checklist:
 - A justification for the change
 - At least 10 thumbs up from the community for the issue
 - A published example (academic or press article) of where neglecting the principle has lead to harm
 - A consideration of related items that already exist, and why this change is needed

# References, reading, and more!

 A robust discussion of data ethics is important for the profession. The goal of this tool is to make it easier to implement ethics review within technical projects. There are lots of great resources if you want to think about data ethics, and we encourage you to do so!

[[**yaml magic here**]]

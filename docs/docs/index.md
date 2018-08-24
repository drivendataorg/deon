<div style="display: inline-block; line-height: 1.8em">&nbsp;</div>

<h1><b>An ethics checklist for data scientists</b></h1>

The conversation about ethics in data science, machine learning, and AI is increasingly important. The goal of _deon_ is to push that conversation forward within data teams.

---

**δέον** • (déon) [n.] (_Ancient Greek_) <small><a href="https://en.wiktionary.org/wiki/%CE%B4%CE%AD%CE%BF%CE%BD#Ancient_Greek" target="_blank" style="text-decoration: none; color: #6d6d6d">wikitionary</a></small>
 > Duty; that which is binding, needful, right, proper. 

--------

_deon_ is a command-line tool that allows you to easily add an ethics checklist to your data science projects. We support creating a new, standalone checklist file or appending a checklist to an existing analysis. _deon_ supports generating a checklist in [many common formats](#supported-file-types) that is ready to be incorporated into your project.

The checklist was inspired by an article written by Mike Loukides, Hilary Mason, and DJ Patil and published by O'Reilly: ["Of Oaths and Checklists"](https://www.oreilly.com/ideas/of-oaths-and-checklists).

# Background and Perspective

We have a very particular perspective with this package that we want to share. This is the position from which we make decisions about contributions, issues, PRs, and other activities in maintaining and supporting the package.

First and foremost, our goal is not to be arbitrators of what ethical concerns merit inclusion. We have a [process for changing the default checklist](#changing-the-checklist), but we believe that many domain-specific concerns are not included and teams will benefit from developing [custom cheklists](#custom-checklists). Not every checklist item will be relevant. We encourage teams to remove items, sections, or mark items as `N/A` as the concerns of their projects dictate. 

Second, we built our initial list from a set of proposed items on [multiple checklists that we referenced](#checklist-citations). We owe a great debt to the thinking that proceeded this, and we look forward to the thoughtful.

Third, we can't define exhaustively every term that appears in the checklist. Some of these terms are open to interpretation or mean different things in different contexts. We recommend that when relevant, users create their own glossary for reference.

Fourth, we are working at a level of abstraction that cannot concretely recommend a specific action (e.g., "remove variable X from your model"). Nearly all of the items on the checklist are meant to provoke discussion among good-faith actors who take their ethical responsibilities seriously. Because of this, most of the items are framed as prompts to discuss or consider. Teams will want to document these discussions and decisions for posterity.

Fifth, we believe the primary benefit of a checklist is ensuring that we don't overlook important work. Sometimes it is difficult with pressing deadlines and a demand to multitask to make sure we do the hard work to think about the big picture. This package is meant to make it easier to find the time to have those discussions. Ethics is hard, and we expect some of the conversations that arise from this checklist may also be hard.

Sixth, we want all the checklist items to be as simple as possible (but no simpler), and to be actionable.

Seventh, we want to avoid any items that strictly fall into the realm of statistical best practices. Instead, we want to highlight the areas where we need to pay particular attention above and beyond best practices.

# Using this Tool

## Prerequisites

 - Python >3.6: Your project need not be Python 3, but you need Python 3 to execute this tool.

## Installation

```
$ pip install deon
```

## Simple usage

We recommend adding a checklist as the first step in your data science project. After creating your project folder, you could run:

```
$ deon -o ETHICS.md
```

This will create a markdown file called `ETHICS.md` that you can add directly to your project.

For simple one-off analyses, you can append the checklist to a Jupyter notebook or RMarkdown file.

```
$ jupyter notebook my-analysis.ipynb

...

$ deon -o my-analysis.ipynb  # appends cells to end of notebook
```

This checklist can be used by individuals or teams to ensure that reviewing the ethical implications of their work is part of every project. The checklist is meant as a jumping-off point, and it should spark deeper and more thourough discussions rather than replace those discussions.


# Supported File Types

Here are the currently supported file types. We will accept pull requests with new file types if there is a strong case for widespread use of that filetype.


- `.md`: markdown
- `.rst`: rst
- `.ipynb`: jupyter
- `.html`: html

# CommandLine Options

```
Usage: main [OPTIONS]

Options:
  -l, --checklist PATH  Override checklist file.
  -f, --format TEXT     Output format. Default is "markdown". Can be one of
                        [markdown, rst, jupyter, html]. File extension used if
                        --output is passed.
  -o, --output PATH     Output file path. Extension can be one of [.md, .rst,
                        .ipynb, .html]
  -c, --clipboard       Whether or not to output to clipboard.
  -w, --overwrite       Overwrite output file if it exists.
                        Default is False.
  --help                Show this message and exit.

```

# Default Checklist

# Data Science Ethics Checklist

## A. Data Collection
------
 - [ ] A.1 If there are human subjects, have those subjects have given informed consent, where users clearly understand what they are consenting to and there was a mechanism in place for gathering consent?
 - [ ] A.2 Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those?
 - [ ] A.3 Have we considered ways to to minimize exposure of PII for example through anonymization or not collecting information that isn't relevant for analysis?

## B. Data Storage
------
 - [ ] B.1 Do we have a plan to protect and secure data (e.g., encryption at rest and in transit, access controls on internal users and third parties, access logs, and up-to-date software)?
 - [ ] B.2 Do we have a mechanism through which an individual can request their personal information be removed?
 - [ ] B.3 Is there a schedule or plan to delete the data after it is no longer needed?

## C. Analysis
------
 - [ ] C.1 Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g., affected community and subject matter experts)?
 - [ ] C.2 Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)?
 - [ ] C.3 Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data?
 - [ ] C.4 Have we ensured that data with PII are not used or displayed unless necessary for the analysis?
 - [ ] C.5 Is the process of generating the analysis auditable if we discover issues in the future?

## D. Modeling
------
 - [ ] D.1 Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory?
 - [ ] D.2 Have we tested model results for fairness with respect to different affected groups (e.g., tested for disparate error rates)?
 - [ ] D.3 Have we considered the effects of optimizing for our defined metrics and considered additional metrics?
 - [ ] D.4 Can we explain in understandable terms a decision the model made in cases where a justification is needed?
 - [ ] D.5 Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood?

## E. Deployment
------
 - [ ] E.1 Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)?
 - [ ] E.2 Is there a way to turn off or roll back the model in production if necessary?
 - [ ] E.3 Do we test and monitor for concept drift to ensure the model remains fair over time?
 - [ ] E.4 Have we taken steps to identify and prevent unintended uses and abuse of the model and do we have a plan to monitor these once the model is deployed?



# Custom Checklists

This is not meant to be the only ethical checklist, but instead we try to capture reasonable defaults that are general enough to be widely useful. For your own projects with particular concerns, we recommend your own `checklist.yml` file that is maintained by your team and passed to this tool with the `-l` flag.

Custom checklists must follow the same schema as `checklist.yml`. There must be a top-level `title` which is a string, and `sections` which is a list. Each section in the list `sections` must have a `title`, a `section_id`, and then a list of `lines`. Each line must have a `line_id` and a `line` string which is the content. The format is as follows:

```
title: TITLE
sections: 
  - title: SECTION TITLE
    section_id: SECTION NUMBER
    lines:
        - line_id: LINE NUMBER
          line: LINE CONTENT
```

# Changing the Checklist

Please see [the framing](#background-and-perspective) for an understanding of our perspective. Given this perspective, we will consider changes to the default checklist that fit with that perspective and follow this process.

Our goal is to have checklist items that are actionable as part of a review of data science work or as part of a plan. Please avoid suggesting items that are too vague (e.g., "do no harm") or too specific (e.g., "remove social security numbers from data"). 

**Note: This process is an experiment and is subject to change based on how well it works. Our goal is to avoid :flame: wars in the issue threads while still making a tool that will make adding an ethics checklist to a project easy.**

To request a change, please file an issue with a title that starts with one of: "CREATE, UPDATE, DELETE". There are FOUR requirements for an issue requesting a change to the checklist:

 - A justification for the change
 - At least 10 thumbs up from the community for the issue
 - A published example (academic or press article) of where neglecting the principle has lead to harm
 - A consideration of related items that already exist, and why this change is different from what exists

# References, reading, and more!

 A robust discussion of data ethics is important for the profession. The goal of this tool is to make it easier to implement ethics review within technical projects. There are lots of great resources if you want to think about data ethics, and we encourage you to do so!

## Checklist citations

We're excited to see so many articles popping up on data ethics! The short list below includes articles that directly informed the content in the checklist as well case studies and discussion provoking 'big-picture' articles.

- [Of oaths and checklists](https://www.oreilly.com/ideas/of-oaths-and-checklists)
- How to build ethics into AI ([Part I](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-i-bf35494cce9) and [Part II](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-ii-a563f3372447))
- [An ethical checklist for data science](https://dssg.uchicago.edu/2015/09/18/an-ethical-checklist-for-data-science/)
- [How to recognize exclusion in AI](https://medium.com/microsoft-design/how-to-recognize-exclusion-in-ai-ec2d6d89f850)
- [Case studies in data ethics](https://www.oreilly.com/ideas/case-studies-in-data-ethics)
- [Technology is biased too. How do we fix it?](https://fivethirtyeight.com/features/technology-is-biased-too-how-do-we-fix-it/)
- [The dark secret at the heart of AI](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/)

## Where things have gone wrong

To make the ideas contained in the checklist more concrete, we've compiled [examples](references.md) of times when things have gone wrong. They're paired these with the checklist questions to help illuminate where in process ethics discussions may have helped provide a course correction.

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
 - `-l / --checklist [PATH]` - If you want to override the built-in checklist with your own.

# Default checklist

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

# Changing the checklist

This is not meant to be the only ethical checklist, but instead we try to capture reasonable defaults that are general enough to be widely useful. For your own projects with particular concerns, we recommend a fork of this repository for long-term maitence. An easy first pass is simply creating a new `checklist.yml` file, and using the `l` flag.

Our goal is to have checklist items that are actionable as part of a review of data science work or as part of a plan. Please avoid suggesting items that are too vague (e.g., "do no harm") or too specific (e.g., "remove social security numbers from data"). 

Note: This process is an experiment and is subject to change based on how well it works. Our goal is to avoid :flame: wars in the issue threads while still making a tool that will make adding an ethics checklist to a project easy.

To request a change, please file an issue with a title that starts with one of: "CREATE, UPDATE, DELETE". There are FOUR requirements for an issue requesting a change to the checklist:
 - A justification for the change
 - At least 10 thumbs up from the community for the issue
 - A published example (academic or press article) of where neglecting the principle has lead to harm
 - A consideration of related items that already exist, and why this change is needed

# References, reading, and more!

 A robust discussion of data ethics is important for the profession. The goal of this tool is to make it easier to implement ethics review within technical projects. There are lots of great resources if you want to think about data ethics, and we encourage you to do so!

### Checklist citations

We're excited to see so many articles popping up on data ethics! The short list below includes articles that directly informed the content in the checklist as well case studies and discussion provoking 'big-picture' articles.

- [Of oaths and checklists](https://www.oreilly.com/ideas/of-oaths-and-checklists)
- How to build ethics into AI ([Part I](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-i-bf35494cce9) and [Part II](https://medium.com/salesforce-ux/how-to-build-ethics-into-ai-part-ii-a563f3372447))
- [An ethical checklist for data science](https://dssg.uchicago.edu/2015/09/18/an-ethical-checklist-for-data-science/)
- [How to recognize exclusion in AI](https://medium.com/microsoft-design/how-to-recognize-exclusion-in-ai-ec2d6d89f850)
- [Case studies in data ethics](https://www.oreilly.com/ideas/case-studies-in-data-ethics)
- [Technology is biased too. How do we fix it?](https://fivethirtyeight.com/features/technology-is-biased-too-how-do-we-fix-it/)
- [The dark secret at the heart of AI](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/)

### Where things have gone wrong

To make the ideas contained in the checklist more concrete, we've compiled [examples](docs/docs/references.md) of times when things have gone wrong. They're paired these with the checklist questions to help illuminate where in process ethics discussions may have helped provide a course correction.


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


Data collection
1. Informed consent -- Tuskagee study http://www.socialworker.com/feature-articles/ethics-articles/The_Tuskegee_Syphilis_Study_and_Its_Implications_for_the_21st_Century/
2. Bias in collection and survey design 
- AI voices https://www.technologyreview.com/s/608619/ai-programs-are-learning-to-exclude-some-african-american-voices/
- face recognition cameras http://content.time.com/time/business/article/0,8599,1954643,00.html, https://www.reuters.com/article/us-newzealand-passport-error/new-zealand-passport-robot-tells-applicant-of-asian-descent-to-open-eyes-idUSKBN13W0RL
3. Collecting non relevant PII
4. Appropriate anonymization -- Netflix https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/

Data storage
1. Secure data -- Equifax
2. Appropriate access controls
3. Abilitly to be removed
4. Data deletion

Exploratory analysis
1. Sources of bias in data
-- criminal justice system https://www.washingtonpost.com/opinions/big-data-may-be-reinforcing-racial-bias-in-the-criminal-justice-system/2017/02/10/d63de518-ee3a-11e6-9973-c5efb7ccfb0d_story.html?utm_term=.0ae23a0f7c49 (opinion)
2. Honest visualizations
3. PII not displayed
4. Auditable analysis

Modeling
1. Address blindspots -- Apple health https://www.theverge.com/2014/9/25/6844021/apple-promised-an-expansive-health-app-so-why-cant-i-track
2. Proxies
3. Fairness wrt different groups
- Gorillas tag -- https://www.forbes.com/sites/mzhang/2015/07/01/google-photos-tags-two-african-americans-as-gorillas-through-facial-recognition-software/#12bdb1fd713d
- Criminal sentencing -- https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
- lending -- https://www.whitecase.com/publications/insight/algorithms-and-bias-what-lenders-need-know
4. Assumptions and optimization implications
5. Explainability -- https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/

Deployment
1. Ability to turn off
2. Mechanism for redress
3. Model drift
4. Abuse, unintended use, attacks -- AI "gaydar"
- https://www.nytimes.com/2017/10/09/science/stanford-sexual-orientation-study.html
- https://osf.io/zn79k/
- https://www.kqed.org/futureofyou/435378/can-facial-recognition-detect-sexual-orientation-controversial-stanford-study-now-under-ethical-review
5. Communicate bias


Resources
- Terminology guide: http://www.datascienceassn.org/code-of-conduct.html
- 

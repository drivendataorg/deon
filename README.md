
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

### Data Collection
------
- If there are human subjects, have those subjects have given informed consent, where users clearly understand what they are consenting to and there was a mechanism in place for gathering consent?
	- [African-American men were enrolled in the Tuskagee Study on the progression of syphillis without being told the true purpose of the study or that treatment for syphillis was being withheld.](https://en.wikipedia.org/wiki/Tuskegee_syphilis_experiment)
- Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those?
	- [Face recognition cameras used for passport control register Asian's eyes as closed](http://content.time.com/time/business/article/0,8599,1954643,00.html). [addtl link](https://www.reuters.com/article/us-newzealand-passport-error/new-zealand-passport-robot-tells-applicant-of-asian-descent-to-open-eyes-idUSKBN13W0RL)
- Have we considered ways to to minimize exposure of PII for example through anonymization or not collecting information that isn't relevant for analysis?
	- [Netflix prize dataset of movie rankings by 500,000 customers is easily de-anonymized through cross referencing with other publicly available datasets.](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/)

### Data Storage
------
- Do we have a plan to protect and secure data (e.g. encryption at rest and in transit, access controls, access logs, and up-to-date software)?
	- Personal and financial data for more than 147 million people was stolen in the Equifax data breach.
	- [AOL accidentally released 20 million search queries from 658,000 customers](https://www.wired.com/2006/08/faq-aols-search-gaffe-and-you/)
- Do we have a mechanism through which an individual can request their personal information be removed?
- Is there a schedule or plan to delete the data after it is no longer needed?

### Analysis
------
- Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g. affected community and subject matter experts)?
	- [When Apple's HealthKit came out in 2014, women couldn't track menstruation](https://www.theverge.com/2014/9/25/6844021/apple-promised-an-expansive-health-app-so-why-cant-i-track)
- Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)?
	- [Criminal sentencing](https://www.washingtonpost.com/opinions/big-data-may-be-reinforcing-racial-bias-in-the-criminal-justice-system/2017/02/10/d63de518-ee3a-11e6-9973-c5efb7ccfb0d_story.html?utm_term=.0ae23a0f7c49)
	- [Women are more likely to be [shown lower-paying jobs than men in Google ads](https://www.theguardian.com/technology/2015/jul/08/women-less-likely-ads-high-paid-jobs-google-study).
- Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data?
- Have we ensured that data with PII are not used or displayed unless necessary for the analysis?
- Is the process of generating the analysis auditable if we discover issues in the future?

### Modeling
------
- Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory?
- Have we tested model results for fairness with respect to different affected groups (e.g. tested for disparate error rates)?
	- [Google Photos tags two African-Americans as gorillas](https://www.forbes.com/sites/mzhang/2015/07/01/google-photos-tags-two-african-americans-as-gorillas-through-facial-recognition-software/#12bdb1fd713d)
	- [Racial bias in criminal sentencing](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
	- [lending](https://www.whitecase.com/publications/insight/algorithms-and-bias-what-lenders-need-know)
	- [Google's speech recognition software doesn't recognize women's voices as well as men's.](https://www.dailydot.com/debug/google-voice-recognition-gender-bias/)
	- [Facial recognition software is significanty worse at identifying people with darker skin.](https://www.theregister.co.uk/2018/02/13/facial_recognition_software_is_better_at_white_men_than_black_women/) [study](http://proceedings.mlr.press/v81/buolamwini18a.html)
	- [word2vec, trained on Google News corpus, reinforces gender stereotypes.](https://www.technologyreview.com/s/602025/how-vector-space-mathematics-reveals-the-hidden-sexism-in-language/) [study](https://arxiv.org/abs/1607.06520), [related blog](https://blog.kjamistan.com/embedded-isms-in-vector-based-natural-language-processing/)
	- [Google searches involving black-sounding names are more likely to serve up ads suggestive of a criminal record than white-sounding names](https://www.technologyreview.com/s/510646/racism-is-poisoning-online-ad-delivery-says-harvard-professor/) [study](https://arxiv.org/abs/1301.6822)
- Have we considered the effects of optimizing for our defined metrics and considered additional metrics?
- Can we explain in understandable terms a decision the model made in cases where a justification is needed?
	-  https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/
- Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood?

### Deployment
------
- Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)?
- Is there a way to turn off or roll back the model in production if necessary?
- Do we test and monitor for model drift to ensure it remains fair over time?
- Have we taken steps to identify and prevent unintended uses and abuse of the model?
	- https://www.nytimes.com/2017/10/09/science/stanford-sexual-orientation-study.html
	- https://osf.io/zn79k/
	- https://www.kqed.org/futureofyou/435378/can-facial-recognition-detect-sexual-orientation-controversial-stanford-study-now-under-ethical-review

### Additional reading
------
- Terminology guide: http://www.datascienceassn.org/code-of-conduct.html


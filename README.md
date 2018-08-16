
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

# Default checklist

### A. Data Collection
------
 - [ ] A.1 If there are human subjects, have those subjects have given informed consent, where users clearly understand what they are consenting to and there was a mechanism in place for gathering consent?
 - [ ] A.2 Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those?
 - [ ] A.3 Have we considered ways to to minimize exposure of PII for example through anonymization or not collecting information that isn't relevant for analysis?

### B. Data Storage
------
 - [ ] B.1 Do we have a plan to protect and secure data (e.g., encryption at rest and in transit, access controls, access logs, and up-to-date software)?
 - [ ] B.2 Do we have a mechanism through which an individual can request their personal information be removed?
 - [ ] B.3 Is there a schedule or plan to delete the data after it is no longer needed?

### C. Analysis
------
 - [ ] C.1 Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g., affected community and subject matter experts)?
 - [ ] C.2 Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)?
 - [ ] C.3 Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data?
 - [ ] C.4 Have we ensured that data with PII are not used or displayed unless necessary for the analysis?
 - [ ] C.5 Is the process of generating the analysis auditable if we discover issues in the future?

### D. Modeling
------
 - [ ] D.1 Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory?
 - [ ] D.2 Have we tested model results for fairness with respect to different affected groups (e.g., tested for disparate error rates)?
 - [ ] D.3 Have we considered the effects of optimizing for our defined metrics and considered additional metrics?
 - [ ] D.4 Can we explain in understandable terms a decision the model made in cases where a justification is needed?
 - [ ] D.5 Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood?

### E. Deployment
------
 - [ ] E.1 Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)?
 - [ ] E.2 Is there a way to turn off or roll back the model in production if necessary?
 - [ ] E.3 Do we test and monitor for model drift to ensure it remains fair over time?
 - [ ] E.4 Have we taken steps to identify and prevent unintended uses and abuse of the model?

# Changing the checklist

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

To make the ideas contained in the checklist more concrete, below are examples of times when things have gone wrong. They're paired these with the checklist questions to help illuminate where in process ethics discussions may have helped provide a course correction.

 Checklist Question | Examples of Ethical Issues
--- | ---
**A.1**. If there are human subjects, have those subjects have given informed consent, where users clearly understand what they are consenting to and there was a mechanism in place for gathering consent? | <ul><li>[African-American men were enrolled in the Tuskagee Study on the progression of syphillis without being told the true purpose of the study or that treatment for syphillis was being withheld.](https://en.wikipedia.org/wiki/Tuskegee_syphilis_experiment)</li></ul>
**A.2**. Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those? | <ul><li>[StreetBump, a smartphone app to passively detect potholes, may fail to direct public resources to areas where smartphone penetration is lower, such as lower income areas or areas with a larger elderly population.](https://hbr.org/2013/04/the-hidden-biases-in-big-data)</li><li>[Facial recognition cameras used for passport control register Asian's eyes as closed.](http://content.time.com/time/business/article/0,8599,1954643,00.html)</li></ul>
**A.3**. Have we considered ways to to minimize exposure of PII for example through anonymization or not collecting information that isn't relevant for analysis? | <ul><li>[Personal information on taxi drivers can be accessed in poorly anonymized taxi trips dataset released by New York City.](https://www.theguardian.com/technology/2014/jun/27/new-york-taxi-details-anonymised-data-researchers-warn)</li><li>[Netflix prize dataset of movie rankings by 500,000 customers is easily de-anonymized through cross referencing with other publicly available datasets.](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/)</li></ul>
**B.1**. Do we have a plan to protect and secure data (e.g., encryption at rest and in transit, access controls, access logs, and up-to-date software)? | <ul><li>[Personal and financial data for more than 146 million people was stolen in Equifax data breach.](https://www.nbcnews.com/news/us-news/equifax-breaks-down-just-how-bad-last-year-s-data-n872496)</li><li>[AOL accidentally released 20 million search queries from 658,000 customers.](https://www.wired.com/2006/08/faq-aols-search-gaffe-and-you/)</li></ul>
**B.2**. Do we have a mechanism through which an individual can request their personal information be removed? | <ul><li>[The EU's General Data Protection Regulation (GDPR) includes the "right to be forgotten."](https://www.eugdpr.org/the-regulation.html)</li></ul>
**B.3**. Is there a schedule or plan to delete the data after it is no longer needed? | <ul><li>[FedEx exposes private information of thousands of customers after a legacy s3 server was left open without a password.](https://www.zdnet.com/article/unsecured-server-exposes-fedex-customer-records/)</li></ul>
**C.1**. Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g., affected community and subject matter experts)? | <ul><li>[When Apple's HealthKit came out in 2014, women couldn't track menstruation.](https://www.theverge.com/2014/9/25/6844021/apple-promised-an-expansive-health-app-so-why-cant-i-track)</li></ul>
**C.2**. Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)? | <ul><li>[word2vec, trained on Google News corpus, reinforces gender stereotypes.](https://www.technologyreview.com/s/602025/how-vector-space-mathematics-reveals-the-hidden-sexism-in-language/)</li><li>[(Study)](https://arxiv.org/abs/1607.06520)</li><li>[Women are more likely to be shown lower-paying jobs than men in Google ads.](https://www.theguardian.com/technology/2015/jul/08/women-less-likely-ads-high-paid-jobs-google-study)</li></ul>
**C.3**. Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data? | <ul><li>[Misleading chart shown at Planned Parenthood hearing distorts actual trends of abortions vs. cancer screenings and preventative services.](https://www.politifact.com/truth-o-meter/statements/2015/oct/01/jason-chaffetz/chart-shown-planned-parenthood-hearing-misleading-/)</li></ul>
**C.4**. Have we ensured that data with PII are not used or displayed unless necessary for the analysis? | <ul><li>[Strava heatmap of exercise routes reveals sensitive information on military bases and spy outposts.](https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases)</li></ul>
**C.5**. Is the process of generating the analysis auditable if we discover issues in the future? | <ul><li>[Excel error in well-known economics paper undermines justification of austerity measures.](https://www.bbc.com/news/magazine-22223190)</li></ul>
**D.1**. Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory? | <ul><li>[Criminal sentencing risk asessments don't ask directly about race or income, but other demographic factors can end up being proxies.](https://www.themarshallproject.org/2015/08/04/the-new-science-of-sentencing)</li><li>[Creditworthiness algorithms based on nontraditional criteria such as grammatic habits, preferred grocery stores, and friends' credit scores can perpetuate systemic bias.](https://www.whitecase.com/publications/insight/algorithms-and-bias-what-lenders-need-know)</li></ul>
**D.2**. Have we tested model results for fairness with respect to different affected groups (e.g., tested for disparate error rates)? | <ul><li>[Google Photos tags two African-Americans as gorillas.](https://www.forbes.com/sites/mzhang/2015/07/01/google-photos-tags-two-african-americans-as-gorillas-through-facial-recognition-software/#12bdb1fd713d)</li><li>[With COMPAS, a risk-assessment algorithm used in criminal sentencing, black defendants are almost twice as likely to be mislabeled as likely to reoffend.](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)</li><li>[Google's speech recognition software doesn't recognize women's voices as well as men's.](https://www.dailydot.com/debug/google-voice-recognition-gender-bias/)</li><li>[Facial recognition software is significanty worse at identifying people with darker skin.](https://www.theregister.co.uk/2018/02/13/facial_recognition_software_is_better_at_white_men_than_black_women/)</li><li>[(Study)](http://proceedings.mlr.press/v81/buolamwini18a.html)</li><li>[Google searches involving black-sounding names are more likely to serve up ads suggestive of a criminal record than white-sounding names.](https://www.technologyreview.com/s/510646/racism-is-poisoning-online-ad-delivery-says-harvard-professor/)</li><li>[(Study)](https://arxiv.org/abs/1301.6822)</li></ul>
**D.3**. Have we considered the effects of optimizing for our defined metrics and considered additional metrics? | <ul><li>[Facebook seeks to optimize "time well spent", prioritizing interaction over popularity.](https://www.wired.com/story/facebook-tweaks-newsfeed-to-favor-content-from-friends-family/)</li><li>[YouTube search autofill suggests pedophiliac phrases due to high viewership of related videos.](https://gizmodo.com/youtubes-creepy-kid-problem-was-worse-than-we-thought-1820763240)</li></ul>
**D.4**. Can we explain in understandable terms a decision the model made in cases where a justification is needed? | <ul><li>[Patients with pneumonia with a history of asthma are usually admitted to the intensive care unit as they have a high risk of dying from pneumonia. Given the success of the intensive care, neural networks predicted that asthmatics had a lower risk of dying and could therefore be sent home. Without explanatory models to identify this issue, patients would have been sent home to die.](http://people.dbmi.columbia.edu/noemie/papers/15kdd.pdf)</li><li>[GDPR includes a "right to explanation," i.e. meaningful information on the logic underlying automated decisions.](hhttps://academic.oup.com/idpl/article/7/4/233/4762325)</li></ul>
**D.5**. Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood? | <ul><li>[Google Flu claims to accurately predict weekly influenza activity and then misses the 2009 swine flu pandemic.](https://www.forbes.com/sites/stevensalzberg/2014/03/23/why-google-flu-is-a-failure/#6fa6a1925535)</li></ul>
**E.1**. Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)? | <ul><li>[Software mistakes result in healthcare cuts for people with diabetes or cerebral palsy.](https://www.theverge.com/2018/3/21/17144260/healthcare-medicaid-algorithm-arkansas-cerebral-palsy)</li></ul>
**E.2**. Is there a way to turn off or roll back the model in production if necessary? | <ul><li>[people getting put on watchlists incorrectly and can't get off](TBD)</li></ul>
**E.3**. Do we test and monitor for model drift to ensure it remains fair over time? | <ul><li>[model drift](TBD)</li></ul>
**E.4**. Have we taken steps to identify and prevent unintended uses and abuse of the model? | <ul><li>[Microsoft's Twitter chatbot Tay quickly becomes racist.](https://www.theguardian.com/technology/2016/mar/24/microsoft-scrambles-limit-pr-damage-over-abusive-ai-bot-tay)</li><li>[Deepfakes -- realistic but fake videos generated through AI -- span the gammut from celebrity porn to presidential statements.](http://theweek.com/articles/777592/rise-deepfakes)</li></ul>


# Data Science Ethics Checklist

## Data Collection
------
 - [ ] If there are human subjects, have those subjects have given informed consent, where users clearly understand what they are consenting to and there was a mechanism in place for gathering consent?
 - [ ] Have we considered sources of bias that could be introduced during data collection and survey design and taken steps to mitigate those?
 - [ ] Have we considered ways to to minimize exposure of PII for example through anonymization or not collecting information that isn't relevant for analysis?

## Data Storage
------
 - [ ] Do we have a plan to protect and secure data (e.g. encryption at rest and in transit, access controls, access logs, and up-to-date software)?
 - [ ] Do we have a mechanism through which an individual can request their personal information be removed?
 - [ ] Is there a schedule or plan to delete the data after it is no longer needed?

## Analysis
------
 - [ ] Have we sought to address blindspots in the analysis through engagement with relevant stakeholders (e.g. affected community and subject matter experts)?
 - [ ] Have we examined the data for possible sources of bias and taken steps to mitigate or address these biases (e.g., stereotype perpetuation, confirmation bias, imbalanced classes, or omitted confounding variables)?
 - [ ] Are our visualizations, summary statistics, and reports designed to honestly represent the underlying data?
 - [ ] Have we ensured that data with PII are not used or displayed unless necessary for the analysis?
 - [ ] Is the process of generating the analysis auditable if we discover issues in the future?

## Modeling
------
 - [ ] Have we ensured that the model does not rely on variables or proxies for variables that are unfairly discriminatory?
 - [ ] Have we tested model results for fairness with respect to different affected groups (e.g. tested for disparate error rates)?
 - [ ] Have we considered the effects of optimizing for our defined metrics and considered additional metrics?
 - [ ] Can we explain in understandable terms a decision the model made in cases where a justification is needed?
 - [ ] Have we communicated the shortcomings, limitations, and biases of the model to relevant stakeholders in ways that can be generally understood?

## Deployment
------
 - [ ] Have we discussed with our organization a plan for response if users are harmed by the results (e.g., how does the data science team evaluate these cases and update analysis and models to prevent future harm)?
 - [ ] Is there a way to turn off or roll back the model in production if necessary?
 - [ ] Do we test and monitor for model drift to ensure it remains fair over time?
 - [ ] Have we taken steps to identify and prevent unintended uses and abuse of the model?


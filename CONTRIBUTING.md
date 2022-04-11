# Contributing

Contributions are welcome, and they are greatly appreciated! Did you read an interesting article about a time where data ethics went awry? Do you see an area the checklist doesn't fully cover? Submit a PR to make an addition!

## Types of contributions

Contributors can add to `deon` by (1) adding an [example](https://deon.drivendata.org/examples/) that helps illustrate the different realms and ramifications of data ethics practices from the checklist and/or (2) changing or adding an item to the [checklist](https://deon.drivendata.org/#data-science-ethics-checklist) itself.

To get started, first `git clone` the [deon repository](https://github.com/drivendataorg/deon/). 

### 1. Adding a new item to the examples table

To add an example:
- [ ] Use the [examples table](https://deon.drivendata.org/examples/) to determine the checklist item to which your article applies.
- [ ] Add the example to the `examples_of_ethical_issues.yml` file.
- [ ] Open a pull request with the change to the yaml file.

#### How to edit the examples table yaml

In [`deon/assets/examples_of_ethical_issues.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/examples_of_ethical_issues.yml), locate the section for the relevant checklist item. Each checklist item corresponds to a specific `line_id` (e.g. "Informed Consent" is A.1). Then:

- [ ] Create a new bullet in the `links` section for that line ID, following the format of other examples.
- [ ] After `text`:, write a succinct one sentence summary of what went wrong.
- [ ] After `url`:, paste the url to the article or research paper.

Your change to the `examples_of_ethical_issues.yml` should look something like this:

```
- text: Facebook uses phone numbers provided for two-factor authentication to target users with ads.
  url: https://techcrunch.com/2018/09/27/yes-facebook-is-using-your-2fa-phone-number-to-target-you-with-ads/
```

### 2. Changing the checklist

Given [our defined perspective on the checklist](#background-and-perspective), we will consider changes to the default checklist that fit with that perspective and follow this process. Our goal is to have checklist items that are actionable as part of a review of data science work or as part of a plan. Please avoid suggesting items that are too vague (e.g., "do no harm") or too specific (e.g., "remove social security numbers from data").

As part of deon's goal to provide concrete, actionable reminders of the influence of data scientists' choices on the ethics of data science projects, each addition to to the checklist must be accompanied by an example.

The steps for this contribution are:
- [ ] Edit the `checklist.yml` file.
- [ ] Add an example to the `examples_of_ethical_issues.yml` file.
- [ ] Open a PR that follows the guidelines below.

#### How to edit the checklist yaml

Navigate to the section of [`deon/assets/checklist.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/checklist.yml) where your addition or change applies (e.g. Data Storage). Then follow the format of the other checklist items in making your contribution:

- [ ] Create a new bullet in the `lines` section for that `line_id`, following the format of other checklist items. Ensure the numbering of all line_ids in the section is sequential.
- [ ] After `line_summary`, describe the topic of your question in a few words.
- [ ] After `line`, add the new checklist question.

#### How to edit the examples table yaml

[See this section above](#how-to-edit-the-examples-table-yaml).

#### Pull request guidelines

 A pull request to add an item to the checklist should change the following files:

  1. [`deon/assets/checklist.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/checklist.yml): contains the default checklist items
  2. [`deon/assets/examples_of_ethical_issues.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/examples_of_ethical_issues.yml): contains example of harms caused when the item was not considered

The description in the pull request must include:
  - A justification for the change
  - A consideration of related items that already exist, and why this change is different from what exists
  - A published example (academic or press article) of where neglecting the principle has lead to concrete harm (articles that discuss potential or hypothetical harm will not be considered sufficient)

## Release process (for maintainers)

The [`release`](https://github.com/drivendataorg/deon/blob/main/.github/workflows/release.yml) GitHub Actions workflow automates the process of releasing a new version of `deon`.

All you need to do kick off the release process is to update the [`VERSION`](https://github.com/drivendataorg/deon/blob/main/VERSION) file and merge the change into the `main` branch. The `release` workflow watches the main branch for changes to this file.

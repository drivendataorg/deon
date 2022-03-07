# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given. You can contribute in several different ways:

## Types of Contributions

Did you read an interesting article about a time where data ethics went awry? Do you see an area the checklist doesn't fully cover? Submit a PR to make an addition!

Contributors can add to Deon by (1) adding an item to the checklist and (2) by adding an example that helps illustrate the different realms and ramifications of data ethics practices. As illustrated in our [Background and perspective section](#background-and-perspective) we have a defined perspective on the checklist, how it is used, and how it is created. Please refer to this section as you make your contribution.

### 1. Changes to the Checklist
Given [our defined perspective on the checklist](#background-and-perspective), we will consider changes to the default checklist that fit with that perspective and follow this process.

Our goal is to have checklist items that are actionable as part of a review of data science work or as part of a plan. Please avoid suggesting items that are too vague (e.g., "do no harm") or too specific (e.g., "remove social security numbers from data").

**Note: This process is an experiment and is subject to change based on how well it works. Our goal is to avoid flame wars in the issue threads while still making a tool that will make adding an ethics checklist to a project easy.**

To request a change, please file an issue with a title that starts with one of: "CREATE, UPDATE, DELETE". There are FOUR requirements for an issue requesting a change to the checklist:

 - A justification for the change
 - At least 10 thumbs up from the community for the issue
 - A published example (academic or press article) of where neglecting the principle has lead to concrete harm (articles that discuss potential or hypothetical harm will not be considered sufficient)
 - A consideration of related items that already exist, and why this change is different from what exists

After filing an issue that meets the above criteria, please `git clone` the [Deon repository](https://github.com/drivendataorg/deon/). In order to contribute to the checklist, you'll need to edit  `deon/deon/assets/checklist.yml`.  

In the section corresponding to your contribution (Data Collection, Data Storage, Analysis, Modeling, or Deployment) in `deon/deon/assets/checklist.yml` you'll need to enter three components:
1. `line_id`: Combine the section ID with the number of the item on the list - for example, "Downstream bias mitigation" under "Data Collection" is A.4. 
2. `line_summary`: Describe the topic of your question in a few words
3. `line`: Enter the question you wish to add to the checklist.

As a part of Deon's goal to provide concrete, actionable reminders of the influence of data scientists' choices on the ethics of data science projects, each addition to to the checklist must be accompanied by an example.

### 2. Adding Examples

Whether you would like to add an example to support a new checklist item or for an existing checklist item, you'll need to edit `deon/deon/assets/examples_of_ethical_issues.yml`. Please `git clone` the [Deon repository](https://github.com/drivendataorg/deon/) to edit this file.

Navigate to the section of `examples_of_ethical_issues.yml` corresponding to your example (e.g., `line_id` A.1 for examples related to informed consent - you can use the [current table](https://deon.drivendata.org/examples/) to determine the checklist item to which your example applies), and follow the format of the other examples listed. 

1. Create a new bullet in the `links` section for that line ID, following the format of other examples.
2. After `text`:, write a succinct one sentence summary of what went wrong.
3. After `url`:, paste the url to the article or research paper.

Your change to the examples_of_ethical_issues.yml should look something like this:

```
- text: Facebook uses phone numbers provided for two-factor authentication to target users with ads.
  url: https://techcrunch.com/2018/09/27/yes-facebook-is-using-your-2fa-phone-number-to-target-you-with-ads/
```

## Preparing Your Contributions

After you've cloned the [Deon repository](https://github.com/drivendataorg/deon/), made changes to either `checklist.yml`, `examples_of_ethical_issues.yml`, or both, you can prepare your changes by running the following at the command line (You should *not* make any changes to markdown files directly):

`make reqs` (This makes sure that you have all the necessary tools installed to prepare your changes. Python 3.6+ and GNU Make are the prerequisites.)

and then

`make build` (This creates the appropriate markdown files for the checklist and the examples table. It also creates the various forms of the examples table - `.rst`, `.txt`, `.ipynb`, etc. - that are available on the Deon site).

## Pull Request Guidelines

 A pull request to add an item to the checklist should change:

  1. [`deon/assets/checklist.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/checklist.yml): contains the default checklist items
  2. [`deon/assets/examples_of_ethical_issues.yml`](https://github.com/drivendataorg/deon/blob/main/deon/assets/examples_of_ethical_issues.yml): contains example of harms caused when the item was not considered
  3. There will be several automatically-generated files in `examples/` that appear after running `make build`. These should also be committed and should not be changed directly by the contributor after they have been generated.

A pull request to add an example should change only (2) and (3) above.

## Release Process (for maintainers)

The [`release`](https://github.com/drivendataorg/deon/blob/main/.github/workflows/release.yml) GitHub Actions workflow automates the process of releasing a new version of `deon`.

All you need to do kick off the release process is to update the [`VERSION`](https://github.com/drivendataorg/deon/blob/main/VERSION) file and merge the change into the `main` branch. The `release` workflow watches the main branch for changes to this file.

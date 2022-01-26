# Contributing

Contributions are welcome, and they are greatly appreciated!

This document is still a work-in-progress. Sorry!

## Release Process (for maintainers)

The [`release`](https://github.com/drivendataorg/deon/blob/main/.github/workflows/release.yml) GitHub Actions workflow automates the process of releasing a new version of `deon`.

All you need to do kick off the release process is to update the [`VERSION`](https://github.com/drivendataorg/deon/blob/main/VERSION) file and merge the change into the `main` branch. The `release` workflow watches the main branch for changes to this file.

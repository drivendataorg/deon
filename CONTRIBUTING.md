# Contributing

Contributions are welcome, and they are greatly appreciated!

This document is still a work-in-progress. Sorry!

## Release Process (for maintainers)

The [`release`](https://github.com/drivendataorg/deon/blob/master/.github/workflows/release.yml) GitHub Actions workflow automates the process of releasing a new version of `deon`.

All you need to do kick off the release process is to update the [`VERSION`](https://github.com/drivendataorg/deon/blob/master/VERSION) file and merge the change into the `master` branch. The `release` workflow watches the master branch for changes to this file.

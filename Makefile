.PHONY: register_hook reqs examples docs test render_markdown

# adds git precommit hook
register_hook:
	cp .precommithook .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

## Install python dependencies
reqs: register_hook
	pip install -r dev-requirements.txt

examples: reqs
	deon --output examples/ethics.md --overwrite
	deon --output examples/ethics.ipynb --overwrite
	deon --output examples/ethics.html --overwrite
	deon --output examples/ethics.rst --overwrite
	deon --output examples/ethics.txt --overwrite


# generates README.md and documentation md pages
render_markdown:
	cd docs && python render_templates.py

docs: render_markdown
	cd docs && mkdocs build

test: lint
	pytest -vv

lint:
	flake8 .

## Run tests and build rendered examples and docs
build: test examples docs

clean_pycache:
	find . -name *.pyc -delete && find . -name __pycache__ -delete

clean: clean_pycache
	rm -rf dist
	rm -rf deon.egg-info

package: build clean
	python setup.py sdist

distribute_pypitest: package
	twine upload --repository pypitest dist/*.tar.gz

distribute_pypi: package
	twine upload --repository pypi dist/*.tar.gz


#################################################################################
# Self Documenting Commands                                                                #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
#   * save line in hold space
#   * purge line
#   * Loop:
#       * append newline + line to hold space
#       * go to next line
#       * if line starts with doc comment, strip comment character off and loop
#   * remove target prerequisites
#   * append hold space (+ newline) to line
#   * replace newline plus comments by `---`
#   * print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) == Darwin && echo '--no-init --raw-control-chars')

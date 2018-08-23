.PHONY: reqs examples docs test

reqs:
	pip install -r dev-requirements.txt

examples: reqs
	ethics-checklist --output examples/ethics.md --overwrite
	ethics-checklist --output examples/ethics.ipynb --overwrite
	ethics-checklist --output examples/ethics.html --overwrite
	ethics-checklist --output examples/ethics.rst --overwrite

docs:
	cd docs && mkdocs build

test: lint
	py.test

lint:
	flake8 .

build: test examples docs
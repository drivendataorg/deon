.PHONY: reqs examples docs test render_markdown

reqs:
	pip install -r dev-requirements.txt

examples: reqs
	ethics-checklist --output examples/ethics.md --overwrite
	ethics-checklist --output examples/ethics.ipynb --overwrite
	ethics-checklist --output examples/ethics.html --overwrite
	ethics-checklist --output examples/ethics.rst --overwrite

# generates README.md and documentation md pages
render_markdown:
	cd docs && python render_templates.py

docs: render_markdown
	cd docs && mkdocs build

test: lint
	py.test

lint:
	flake8 .

build: test examples docs

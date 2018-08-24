.PHONY: register_hook reqs examples docs test render_markdown

# adds git precommit hook
register_hook:
	cp .precommithook .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

reqs: register_hook
	pip install -r dev-requirements.txt

examples: reqs
	deon --output examples/ethics.md --overwrite
	deon --output examples/ethics.ipynb --overwrite
	deon --output examples/ethics.html --overwrite
	deon --output examples/ethics.rst --overwrite

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

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
	deon --output examples/ethics.txt --overwrite


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

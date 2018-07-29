.PHONY = reqs examples docs test

reqs:
	pip install -r dev-requirements.txt

examples: reqs
	ethics-checklist --output examples/ethics.md --overwrite
	ethics-checklist --output examples/ethics.ipynb --overwrite

docs:
	echo "NYI"

test: reqs
	echo "NYI"

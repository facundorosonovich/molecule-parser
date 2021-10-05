lint:
	pipenv run pylint src

test: lint
	pipenv run pytest -s --junitxml=test-results/test-results.xml


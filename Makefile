lint:
	pipenv run pylint src

test: lint
	pipenv run pytest -s

test_watch: test
	pipenv run watchmedo shell-command \
 		--patterns="*.py" \
 		--recursive \
 		--command='make test' \
 		.

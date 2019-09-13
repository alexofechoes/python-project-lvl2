install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=gendiff tests  --cov-report xml

analize:
	poetry run mypy gendiff
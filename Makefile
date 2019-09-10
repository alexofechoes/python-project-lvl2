install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

testcoverage:
	poetry run pytest --cov=gendiff tests



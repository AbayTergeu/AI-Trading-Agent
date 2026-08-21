.PHONY: install run test lint format

install:
	pip install -e ".[dev]"

run:
	python -m app.main

test:
	pytest

lint:
	ruff check app tests

format:
	ruff format app tests

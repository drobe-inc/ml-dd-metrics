init:
	poetry install

style:
	poetry run isort src
	poetry run black src 
	poetry run flake8 src --ignore E501

lint:
	poetry run flake8 src --ignore E501
	poetry run isort src
	poetry run black src --check 

test:
	poetry run python -m pytest

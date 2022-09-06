init:
	poetry install

style:
	poetry run isort drobe_dd_metrics
	poetry run black drobe_dd_metrics 
	poetry run flake8 drobe_dd_metrics --ignore E501

lint:
	poetry run flake8 drobe_dd_metrics --ignore E501
	poetry run isort drobe_dd_metrics
	poetry run black drobe_dd_metrics --check 

test:
	poetry run python -m pytest

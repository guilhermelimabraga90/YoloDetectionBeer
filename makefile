.PHONY: install
install: ## Install Python requirements.
	pip install  poetry
	poetry install ultralytics



.PHONY: run
run: ## Run the project.
	poetry  run python ./src/app/__main__.py


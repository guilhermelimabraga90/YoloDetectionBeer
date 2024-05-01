.PHONY: install
install: ## Install Python requirements.
	pip install  poetry
	poetry lock
	poetry install --no-root



.PHONY: run
run: ## Run the project.
	poetry  run python ./src/app/__main__.py


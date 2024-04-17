.PHONY: install
install: ## Install Python requirements.
	python -m pip install --upgrade pip setuptools wheel poetry
	python -m pip install ultralytics



.PHONY: run
run: ## Run the project.
	python ./src/app/__main__.py


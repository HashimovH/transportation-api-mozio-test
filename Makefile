.PHONY: help
.DEFAULT_GOAL := help

-include .env

install: ## Install requirements
    pip install -r requirements.dev.txt

clean:  ## Uninstall dev requirements    
	pip freeze | xargs pip uninstall -y

lock compile: ## Compile all requirements files
    pip-compile --no-emit-index-url --no-header --verbose requirements.in    
	pip-compile --no-emit-index-url --no-header --verbose requirements.dev.in

upgrade: ## Upgrade requirements files
    pip-compile --no-emit-index-url --no-header --verbose --upgrade requirements.in    
	pip-compile --no-emit-index-url --no-header --verbose --upgrade requirements.dev.in

fmt format: ## Run code formatters
    isort app tests    
	black app tests

lint: ## Run code linters
    isort --check app tests    
	black --check app tests
    flake8 app tests    
	mypy core tests
    yamllint --strict .

test: ## Run unit tests with coverage    
	python -m pytest tests/unit --lf --durations=5
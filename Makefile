PACKAGE      = opsduty-client
BASE  	     = $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

POETRY      = poetry

V = 0
Q = $(if $(filter 1,$V),,@)
M = $(shell printf "\033[34;1m▶\033[0m")

.PHONY: all
all: lint test ; @ ## Lint and test project
	$Q

$(POETRY): ; $(info $(M) checking POETRY…)
	$Q

$(BASE): | $(POETRY) ; $(info $(M) checking PROJECT…)
	$Q


.PHONY: test
test: test-pytest | $(BASE) ; @ ## Run tests
	$Q

.PHONY: lint
lint: lint-ruff-format lint-ruff lint-mypy | $(BASE) ; @ ## Run linters
	$Q

.PHONY: fix
fix: fix-ruff-format fix-ruff  | $(BASE) ; @ ## Run fixers
	$Q

# API generator

.PHONY: generate-api-client
generate-api-client: .venv | $(BASE) ; $(info $(M) running api generator…) @ ## Run API generator
	$Q cd $(BASE) && $(POETRY) run openapi-python-client generate \
		--url https://opsduty.io/api/v1/openapi.json \
		--meta poetry \
		--overwrite \
		--output-path opsduty-client \
		--custom-template-path templates/ \
		--config config.yml
	$Q cd $(BASE) && make fix

# Tests

.PHONY: test-pytest
test-pytest: .venv | $(BASE) ; $(info $(M) running api client tests…) @ ## Run pytest
	$Q cd $(BASE) && $(POETRY) run pip install ./opsduty-client
	$Q cd $(BASE) && PYTHONHASHSEED=0 $(POETRY) run pytest

# Fixers

.PHONY: fix-ruff
fix-ruff: .venv | $(BASE) ; $(info $(M) running ruff…) @ ## Run ruff linter
	$Q cd $(BASE) && $(POETRY) run ruff check --fix --unsafe-fixes tests opsduty-client

.PHONY: fix-ruff-format
fix-ruff-format: .venv | $(BASE) ; $(info $(M) running ruff format…) @ ## Run ruff format linter
	$Q cd $(BASE) && $(POETRY) run ruff format tests opsduty-client

# Linters

.PHONY: lint-ruff
lint-ruff: .venv | $(BASE) ; $(info $(M) running ruff…) @ ## Run ruff linter
	$Q cd $(BASE) && $(POETRY) run ruff check tests opsduty-client

.PHONY: lint-ruff-format
lint-ruff-format: .venv | $(BASE) ; $(info $(M) running ruff format…) @ ## Run ruff format linter
	$Q cd $(BASE) && $(POETRY) run ruff format --check tests opsduty-client

.PHONY: lint-mypy
lint-mypy: .venv | $(BASE) ; $(info $(M) running mypy…) @ ## Run mypy linter
	$Q cd $(BASE) && $(POETRY) run mypy tests opsduty-client

# Release
.PHONY: release
release: .venv | $(BASE) ; $(info $(M) running release…) @ ## Run poetry release
	$Q cd $(BASE)/opsduty-client && $(POETRY) publish --build --username=__token__ --password=$(PYPI_TOKEN)

# Dependency management

.venv: pyproject.toml poetry.lock | $(BASE) ; $(info $(M) retrieving dependencies…) @ ## Install python dependencies
	$Q cd $(BASE) && $(POETRY) run pip install -U pip
	$Q cd $(BASE) && $(POETRY) install
	@touch $@

# Misc

.PHONY: clean
clean: ; $(info $(M) cleaning…) @ ## Cleanup caches and virtual environment
	@rm -rf .eggs *.egg-info .venv test-reports node_modules
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +

.PHONY: help
help: ## This help message
	@grep -E '^[ a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort

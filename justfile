# use PowerShell instead of sh:
set shell := ["powershell.exe", "-c"]

ARGS_TEST := env("_UV_RUN_ARGS_TEST", "")
ARGS_RUN := env("_UV_RUN_ARGS_RUN", "")

@_:
    just --list

# run file *args:
#     uv run {{ file }} {{ args }}

# Run app
[group('run')]
run *args:
    uv run {{ ARGS_RUN }} -m vanguard_lib.app {{ args }}

# Run tests
[group('qa')]
test *args:
    uv run {{ ARGS_TEST }} -m pytest {{ args }}

[group('qa')]
_cov *args:
    uv run -m coverage {{ args }}

[group('qa')]
@cov:
    just _cov erase
    just _cov run -m pytest tests
    just _cov combine
    just _cov report
    just _cov html

# Run linters
[group('qa')]
lint:
    uvx ruff check
    uvx ruff format

# Check types
[group('qa')]
typing:
    uvx ty check --python .venv src --output-format concise

# Perform all checks
[group('qa')]
check-all: lint cov typing


_rmdir dir:
    @if (Test-Path "{{ dir }}") { rm -r -force {{ dir }}}

_find_remove dir matching:
    @Get-ChildItem -Path "{{ dir }}" -Recurse -Directory \
        | Where-Object { $_.Name -eq "{{ matching }}" } \
        | rm -r -force


# Update dependencies
[group('lifecycle')]
update:
    uv sync --upgrade

#Ensure project virtualenv is up to date
[group('lifecycle')]
install:
    uv sync

# Remove temporary files
[group('lifecycle')]
clean:
    just _rmdir .venv
    just _rmdir .pytest_cache
    just _rmdir .ruff_cache
    just _rmdir output
    just _rmdir htmlcov
    just _find_remove . __pycache__


# Recreate project virtualenv from nothing
[group('lifecycle')]
fresh: clean install

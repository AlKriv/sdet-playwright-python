# SDET Playwright (Python) Framework

Production-style UI automation framework using **Playwright + Pytest** with:
- **GitHub Actions CI**
- **Screenshots + Playwright traces** on UI test failures
- Configuration via environment variables (**BASE_URL**, **BROWSER**, **HEADLESS**)
- Python linting with **ruff**

## Requirements
- Python 3.11+
- Playwright browsers installed (`python -m playwright install`)
- (Optional) Docker Desktop (later for AWS/EC2 demo)

## Quick start (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install

# run tests (default excludes debug tests)
pytest

# UI smoke only
pytest -m "ui and smoke"

# debug-only tests (excluded by default)
pytest -m debug

# lint
ruff check .

# env vars example
$env:BASE_URL="https://example.com"
$env:BROWSER="firefox"
$env:HEADLESS="0"
pytest -m "ui and smoke"
```

## Environment variables
- `BASE_URL` - target environment base URL (default: https://example.com)
- `BROWSER` - `chromium` (default) / `firefox` / `webkit`
- `HEADLESS` - `1` (default) or `0` to run headed (visible browser)

## Artifacts
On UI test failures the framework saves:
- `artifacts/<test_name>.png` (screenshot)
- `artifacts/<test_name>.zip` (Playwright trace)

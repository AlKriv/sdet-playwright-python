import os

# Base URL can be overridden via BASE_URL env var
BASE_URL = os.getenv("BASE_URL", "https://example.com")

# Browser engine: chromium (default), firefox, webkit $env:BROWSER="firefox"
BROWSER = os.getenv("BROWSER", "chromium").strip().lower()


def _env_bool(name: str, default: str = "1") -> bool:
    """
    Convert env var to bool.
    Accepts: 1/0, true/false, yes/no (case-insensitive).
    """
    value = os.getenv(name, default).strip().lower()
    return value in ("1", "true", "yes", "y", "on")

# Headless mode is default for CI; set HEADLESS=0 to see the browser locally  $env:HEADLESS="0"
HEADLESS = _env_bool("HEADLESS", "1")

# Default timeouts (ms) to make runs consistent across environments
ACTION_TIMEOUT_MS = int(os.getenv("ACTION_TIMEOUT_MS", "10000"))
NAVIGATION_TIMEOUT_MS = int(os.getenv("NAVIGATION_TIMEOUT_MS", "30000"))

# Default viewport size
VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1366"))
VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "768"))
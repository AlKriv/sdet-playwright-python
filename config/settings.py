import os

# Base URL for the environment under test.
# Can be overridden via BASE_URL environment variable.
BASE_URL = os.getenv("BASE_URL", "https://example.com")
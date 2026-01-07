from typing import Any, Dict, Optional

import requests


class ApiClient:
    def __init__(self, base_url: str, token: Optional[str] = None):
        # Base URL for API, e.g. https://api.example.com
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # Optional auth token support (will be used later)
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

        self.session.headers.update({"Accept": "application/json"})

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        # Generic GET wrapper
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, params=params, timeout=10)

import os
from typing import Any, Dict, Optional

import requests


class ApiClient:
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # If token is not provided explicitly, try env var
        token = token or os.getenv("API_TOKEN")

        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

        self.session.headers.update({"Accept": "application/json"})

    def get_headers(self) -> Dict[str, str]:
        # Useful for debugging and assertions in tests
        return dict(self.session.headers)

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, params=params, timeout=10)

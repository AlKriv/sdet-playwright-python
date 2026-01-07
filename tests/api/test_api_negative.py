import os
import pytest

from api.client import ApiClient

BASE_URL = os.getenv("API_BASE_URL", "https://httpbin.org")


@pytest.mark.api
@pytest.mark.smoke
def test_bearer_requires_token_returns_401():
    # No token provided -> should be unauthorized
    client = ApiClient(base_url=BASE_URL, token=None)
    resp = client.get("/bearer")
    assert resp.status_code == 401


@pytest.mark.api
@pytest.mark.smoke
def test_status_403():
    # Explicit 403 endpoint
    client = ApiClient(base_url=BASE_URL)
    resp = client.get("/status/403")
    assert resp.status_code == 403


@pytest.mark.api
@pytest.mark.smoke
def test_status_400():
    # Explicit 400 endpoint
    client = ApiClient(base_url=BASE_URL)
    resp = client.get("/status/400")
    assert resp.status_code == 400

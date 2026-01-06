import os
import pytest

from api.client import ApiClient

@pytest.mark.api
@pytest.mark.smoke
def test_api_health_smoke():
    # Using httpbin as a stable public target for a first smoke test
    base_url = os.getenv("API_BASE_URL", "https://httpbin.org")
    client = ApiClient(base_url=base_url)

    resp = client.get("/status/200")
    assert resp.status_code == 200

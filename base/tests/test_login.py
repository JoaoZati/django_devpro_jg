import pytest as pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_from_page(resp):
    assert resp.status_code == 200

from django.test import Client
import pytest

from pypro.django_assertions import assert_contains
from django.urls import reverse

@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp):
    assert_contains(resp, '<title>Python Pro João Guilherme</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Python Pro JG</a>')

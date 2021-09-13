from django.test import Client # noqa
import pytest

from pypro.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp):
    assert_contains(resp, '<title>Python Pro João Guilherme-Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro JG</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')

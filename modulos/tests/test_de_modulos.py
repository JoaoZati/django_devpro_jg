from django.test import Client # noqa
import pytest

from modulos.models import Modulo
from pypro.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_urls_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())

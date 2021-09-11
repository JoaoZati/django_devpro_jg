import pytest
from model_mommy import mommy
from django.urls import reverse

from aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture  # slug que existe
def resp(client, video):
    print('resp')
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture  # slug que nao existe
def resp_video_nao_encontrado(client, video):
    print('resp')
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))
    # concatenado com conteudo que nao existe


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}')

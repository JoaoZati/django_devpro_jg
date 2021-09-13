from typing import List

from modulos.models import Modulo


def listar_metodos_ordenados() -> List[Modulo]:
    """

    Lista Modulos ordenados por Titulos
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)

from modulos.models import Modulo
from typing import List


def listar_modulos_ordenados() -> List[Modulo]:
    """

    Lista módulos ordenados por titulos
    :return:
    """

    return list(Modulo.objects.order_by('titulo').all())

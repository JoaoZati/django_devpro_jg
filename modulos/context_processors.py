from modulos import facade


def listar_modulos(request):
    return {'MODULOS': facade.listar_metodos_ordenados()}

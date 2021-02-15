from libpython.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='fabricio')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='fabricio'), Usuario(nome='bribaneti')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

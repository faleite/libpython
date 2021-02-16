from libpython.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='fabricio', email='fabricio_2310@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='fabricio', email='fabricio_2310@hotmail.com'),
        Usuario(nome='bribaneti', email='fabricio_2310@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

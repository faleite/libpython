from libpython.spam.db import Conexao
from libpython.spam.modelos import Usuario


def test_salvar_usuario():
    conexao = Conexao()  # Etapa de setup -> conexão com banco de dados
    sessao = conexao.gerar_sessao()  # Etapa de setup -> conexão com banco de dados
    usuario = Usuario(nome='fabricio')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()  # Etapa de teardown -> encerramento da con.banco dados
    sessao.fechar()  # Etapa de teardown -> encerramento da con.banco dados
    conexao.fechar()  # Etapa teardown -> encerramento da con.banco dados


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='fabricio'), Usuario(nome='bribaneti')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

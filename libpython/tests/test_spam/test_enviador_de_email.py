from libpython.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'fabricio_2310@hotmail.com',
        'bribaneti@gmail.com',
        'Cursos Python Faleite',
        'Turma Thiago Avelino aberta.'
    )
    assert 'fabricio_2310@hotmail.com' in resultado

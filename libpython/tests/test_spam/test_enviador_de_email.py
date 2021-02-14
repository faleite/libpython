import pytest

from libpython.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'fabricio_2310@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'bribaneti@gmail.com',
        'Cursos Python Faleite',
        'Turma Thiago Avelino aberta.'
    )
    assert destinatario in resultado

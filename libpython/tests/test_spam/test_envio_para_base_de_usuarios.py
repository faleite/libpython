from unittest.mock import Mock

import pytest

# from libpython.spam.enviador_de_email import Enviador
from libpython.spam.main import EnviadorDeSpam
from libpython.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='fabricio', email='fabricio_2310@hotmail.com'),
            Usuario(nome='bribaneti', email='fabricio_2310@hotmail.com')
        ],
        [
            Usuario(nome='fabricio', email='fabricio_2310@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fabricio_2310@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='fabricio', email='fabricio_2310@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bribaneti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'bribaneti@gmail.com',
        'fabricio_2310@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

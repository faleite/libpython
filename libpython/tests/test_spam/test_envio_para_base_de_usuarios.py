import pytest

from libpython.spam.enviador_de_email import Enviador
from libpython.spam.main import EnviadorDeSpam
from libpython.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fabricio_2310@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='fabricio', email='fabricio_2310@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bribaneti@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'bribaneti@gmail.com',
        'fabricio_2310@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

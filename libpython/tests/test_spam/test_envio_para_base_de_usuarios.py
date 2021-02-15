from libpython.spam.enviador_de_email import Enviador
from libpython.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'fabricio_2310@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

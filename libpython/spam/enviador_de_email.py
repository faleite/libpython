class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'email de remetente invaálido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass

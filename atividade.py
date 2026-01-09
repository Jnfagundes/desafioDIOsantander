#estração
usuarios = [
    {"nome": "Ana", "conta": "12345-6", "cartao": "**** **** **** 1234"},
    {"nome": "Bruno", "conta": "98765-4", "cartao": "**** **** **** 9876"},
    {"nome": "Carla", "conta": "45678-9", "cartao": "**** **** **** 4567"}
]

#transformação
def gerar_mensagem(usuario):
    return (
        f"Olá {usuario['nome']}! 😊\n"
        f"Sua conta {usuario['conta']} está ativa.\n"
        f"Use seu cartão {usuario['cartao']} com segurança!"
    )

mensagens = []

for usuario in usuarios:
    mensagem = gerar_mensagem(usuario)
    mensagens.append(mensagem)

#carregamento
with open("mensagens.txt", "w", encoding="utf-8") as arquivo:
    for msg in mensagens:
        arquivo.write(msg + "\n\n")

#extração
import csv

lista = []

with open("lista.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        lista.append(linha)


#transformação
for usuario in lista:
    usuario["mensagem"] = (
        f"Olá {usuario['nome']}! 👋 "
        f"Sua conta {usuario['conta']} foi analisada com sucesso."
    )

#carregamento
with open("mensagens_geradas.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "conta", "cartao", "mensagem"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
    for usuario in lista:
        escritor.writerow(usuario)

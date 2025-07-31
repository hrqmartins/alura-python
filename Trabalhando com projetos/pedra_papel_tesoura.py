'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao 
usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção.
O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.

roblema central: O problema central é criar um jogo de Pedra, Papel e Tesoura, onde o usuário faz uma escolha e o computador 
escolhe aleatoriamente uma opção. O programa deve então comparar as escolhas e exibir o vencedor.

Etapas do processo:

Passo 01 - Definir as opções do jogo

Criar uma função para salvar a lógica do jogo: def pedra_papel_tesoura()
Criar uma lista opcoes contendo as três escolhas possíveis: "pedra", "papel" e "tesoura".
Passo 02 - Obter a escolha do jogador e do computador

Pedir ao usuário para digitar sua escolha e converter o texto para minúsculas com .lower() para evitar problemas de formatação.
Garantir que a entrada seja válida, verificando se está na lista opcoes.
Gerar a escolha do computador de forma aleatória usando random.choice(opcoes).
Passo 03 - Comparar as escolhas e determinar o vencedor

Exibir a escolha do computador.
Se as duas escolhas forem iguais, exibir "Empate!".
Se o usuário escolheu um item que vence a opção do computador, exibir "Você venceu!".
Caso contrário, exibir "Você perdeu!".
Passo 04 - Exibir o resultado do jogo

Imprimir a escolha do computador e o resultado da partida.
'''

import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

    if escolha_usuario not in opcoes:
        print("Escolha inválida!")
        return

    print(f"Computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (
        (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
        (escolha_usuario == "papel" and escolha_computador == "pedra") or
        (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!")

pedra_papel_tesoura()

'''
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe 
um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores 
inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar 
um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

Problema central: O desafio é criar um jogo interativo onde o usuário deve adivinhar um número gerado aleatoriamente pelo programa. Além disso, o código precisa lidar corretamente com entradas inválidas para evitar falhas durante a execução.

Etapas do processo:

Passo 01 - Gerar o número aleatório

Utilizar random.randint(1, 100) para definir um número secreto entre 1 e 100.
Criar uma variável para contar o número de tentativas do usuário.
Passo 02 - Criar o loop para interação

Utilizar um loop infinito (while True) para manter o jogo ativo até que o usuário acerte o número.
Passo 03 - Capturar a entrada do usuário e validar o valor

Utilizar input() para pedir um número ao usuário.
Utilizar try-except para capturar erros ao converter a entrada em inteiro.
Se o número não estiver no intervalo de 1 a 100, lançar uma exceção ValueError.
Passo 04 - Comparar o palpite com o número secreto

Se o número for menor, exibir "Muito baixo! Tente novamente.".
Se for maior, exibir "Muito alto! Tente novamente.".
Se o usuário acertar, exibir "Parabéns! Você acertou!" e encerrar o jogo.
Passo 05 - Exibir e tratar mensagens de erro

Se o usuário digitar algo que não seja um número, exibir uma mensagem amigável.
Se o número estiver fora do intervalo, exibir um aviso explicando a regra.
'''

import random
 
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
 
    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))
 
            if not 1 <= palpite <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
 
            tentativas += 1
 
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
 
        except ValueError as e:
            print(f"Entrada inválida: {e}")
 
adivinhar_numero()
'''
Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que
extraia trechos importantes de qualquer palavra digitada.

Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.
'''

texto = input("Digite a palavra-chave: ")  
primeiras = texto[:3]
ultimas = texto[-3:]
print(f"Primeiras: {primeiras}")
print(f"Últimas: {ultimas}")
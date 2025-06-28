'''
Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa 
escrever um programa que percorra a lista de nomes e exiba cada cliente.
Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e
explique por que escolheu esse laço.

Eu escolhi o laço for porque ele é mais adequado para percorrer listas quando o número de iterações é conhecido. Como temos uma lista fixa de 
5 clientes, o for é mais simples.

'''

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)
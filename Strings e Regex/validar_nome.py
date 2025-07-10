'''
Lorena trabalha no setor de cadastros de uma empresa e precisa garantir que os nomes inseridos pelos clientes estejam no formato correto. O padrão esperado é
que os nomes comecem com uma letra maiúscula e contenham apenas letras (sem números ou caracteres especiais). Para facilitar o trabalho, ela quer um programa que
valide automaticamente os nomes fornecidos.

Ajude a Lorena criando um programa que solicite um nome ao usuário e verifique se ele atende às regras.
'''

import re

nome = input("Digite o nome do cliente para validação: ")  
if re.fullmatch(r'[A-Z][a-z]*', nome):
    print("Nome válido!")
else:
    print("Nome inválido!")
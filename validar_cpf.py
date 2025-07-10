'''
Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando seus números de CPF no formato 
correto antes de registrar os dados no sistema.

O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.
'''

import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")
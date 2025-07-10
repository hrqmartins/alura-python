'''
Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados. Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". 
Por exemplo, “Monalisa Silva - 1994”.

Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.

Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.
'''

import re

dados = input("Digite o nome completo e o ano de nascimento do paciente: ")  
padrao = r'(\w+) (\w+) - (\d{4})'  

resultado = re.search(padrao, dados)

if resultado:
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano_nascimento = resultado.group(3)

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido!")
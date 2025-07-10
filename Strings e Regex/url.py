'''
Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. Esses critérios são obrigatórios para que o site seja aprovado no 
cadastro. Ajude Renan a criar um programa que realize essa validação de forma automática.

Como você escreveria um programa que peça ao usuário uma URL e informe se ela é válida ou inválida?
'''

url = input("Digite a URL para validação: ")
https = url.startswith("https://")
com = url.endswith(".com")

if https and com:
    print("A URL é válida.")
else:
    print("A URL é inválida.")
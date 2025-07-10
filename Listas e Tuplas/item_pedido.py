'''
Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, mas percebeu que o último foi inserido 
por engano e precisa removê-lo.

Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o 
último item automaticamente.
'''

pedidos = input("Pedidos feitos (separados por vírgula): ").split(", ")
pedidos.pop()
print("Pedidos finais:")
print(pedidos)
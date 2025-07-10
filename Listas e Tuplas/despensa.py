'''
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa.
Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
'''

despensa = ["arroz", "feijão", "macarrão", "açúcar", "sal"]
item = input("Digite o item que deseja verificar: ")
if item in despensa:
    print(f"{item} já está na despensa.")
else:
    print(f"{item} não está na despensa. Você precisa comprar.")
print(despensa)
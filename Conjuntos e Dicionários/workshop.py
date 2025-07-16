'''
Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram
do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados 
do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, 
caso exista.
'''


participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

nome_remover = input("Digite o nome do participante a ser removido: ") 

for workshop, nomes in participantes.items(): 

    nomes.discard(nome_remover) 

print("Lista atualizada de participantes:") 

for workshop, nomes in participantes.items(): 

    print(f"{workshop}: {nomes}") 
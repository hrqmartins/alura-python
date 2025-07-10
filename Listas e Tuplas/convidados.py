'''
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de 
chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e 
organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida 
e exiba a lista atualizada?
'''

convidados = ['Ana', 'Pedro', 'Carlos']
print(f"Lista atual de convidados: {convidados}")
novo_convidado = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
convidados.insert(posicao - 1, novo_convidado)  
print(f"Lista atualizada de convidados: {convidados}")
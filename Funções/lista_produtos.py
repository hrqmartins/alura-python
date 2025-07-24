'''
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com 
seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado
ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato produto: preço
'''

produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 
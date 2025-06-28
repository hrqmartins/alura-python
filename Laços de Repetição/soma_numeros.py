'''
Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para
entender o desempenho financeiro semanal.
Crie um programa para implementar a soma.
'''

valores = [10, 20, 30, 40, 50]
soma = 0

for valor in valores:
    soma += valor
    
print(f"A soma total dos produtos é: {soma}")
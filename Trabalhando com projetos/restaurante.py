'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta.
O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba 
o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor 
gorjeta e o total a ser pago.

Problema central: O problema central é determinar o valor total da conta após adicionar uma gorjeta opcional, calculada como uma porcentagem do valor inicial.

Etapas do processo:

Passo 01 - Receber os dados de entrada

Pedir ao usuário o valor da conta.
Pedir ao usuário a porcentagem de gorjeta desejada.
Converter as entradas para float para garantir precisão nos cálculos.
Passo 02 - Calcular o valor da gorjeta com base na fórmula: gorjeta = (porcentagem_gorjeta / 100) * valor_conta

Passo 03 - Calcular o total a pagar, somando o valor da conta com o valor da gorjeta

Passo 04 - Exibir os resultados formatados

Mostrar o valor da gorjeta com duas casas decimais.
Mostrar o total a pagar, também formatado corretamente.
'''


valor_conta = float(input("Digite o valor da conta: ")) 
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: ")) 
gorjeta = (porcentagem_gorjeta / 100) * valor_conta 
total_a_pagar = valor_conta + gorjeta 
print(f"Valor da gorjeta: R$ {gorjeta:.2f}") 
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
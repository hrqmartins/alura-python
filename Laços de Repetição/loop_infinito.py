'''
André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou 
de responder, e suspeita que o problema está em um loop infinito.

R: Um loop infinito ocorre quando a condição de parada nunca é alcançada, fazendo com que o programa fique preso executando o loop indefinidamente.
Para evitar isso, é necessário garantir que o valor do contador seja atualizado dentro do loop, permitindo que a condição seja eventualmente falsa.
'''

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1 # Atualiza o contador para evitar o loop infinito
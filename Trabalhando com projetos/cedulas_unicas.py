'''
Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O 
caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: 
R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar
o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros 
de entrada caso não seja digitado um valor numérico válido.

Problema central: O desafio é desenvolver um programa que simule o saque de dinheiro em um caixa eletrônico, garantindo que o valor seja válido e utilizando a menor quantidade possível de cédulas disponíveis.

Etapas do processo:

Passo 01 - Definir as cédulas disponíveis

Criar uma lista cedulas contendo os valores disponíveis: 100, 50, 20, 10, 5 e 2.
O caixa não possui cédulas de R$ 1, então o valor deve ser múltiplo de 2.
Passo 02 - Solicitar o valor do saque

Pedir ao usuário que digite um valor para o saque.
Converter a entrada para int, garantindo que seja um número inteiro.
Passo 03 - Validar o valor inserido

Se o valor for menor ou igual a 0, exibir "Erro: O valor deve ser positivo."
Se o valor não for múltiplo de 2, exibir "Erro: O valor deve ser múltiplo de 2."
Passo 04 - Calcular a quantidade de cédulas necessárias

Percorrer a lista de cédulas do maior para o menor valor.
Para cada cédula, calcular quantas são necessárias utilizando valor // cedula.
Atualizar o valor restante com valor % cedula.
Se houver pelo menos uma cédula desse valor, exibir a quantidade entregue.
Passo 05 - Tratar erros de entradas inválidas

Se o usuário inserir um valor não numérico, capturar a exceção ValueError e exibir "Erro: Digite um valor numérico válido."
'''

def caixa_eletronico(): 
    cedulas = [100, 50, 20, 10, 5, 2] 
 
    try: 
        valor = int(input("Digite o valor do saque: ")) 
 
        if valor <= 0: 
            print("Erro: O valor deve ser positivo.")
        elif valor % 2 != 0: 
            print("Erro: O valor deve ser múltiplo de 2.")
        else: 
            print("Cédulas entregues:")
            
            for cedula in cedulas: 
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    valor = valor % cedula 
 
    except ValueError: 
        print("Erro: Digite um valor numérico válido.") 
 
caixa_eletronico()
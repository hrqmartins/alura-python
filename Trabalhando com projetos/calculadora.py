'''
Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, 
ele precisa tratar os erros.

Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código
em funções, use try-except para tratar erros de entrada inválida, que consiste em:

Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

Problema central: O desafio é criar uma calculadora que execute operações matemáticas básicas, garantindo que o programa não 
quebre caso o usuário insira entradas inválidas. Para isso, utilizamos try-except para capturar erros e modularizamos o código 
em funções para melhor organização.

Etapas do processo:

Passo 01 - Criar funções para cada operação

Definir a função somar(num1, num2) que retorna a soma de dois números.
Definir a função subtrair(num1, num2) que retorna a subtração de dois números.
Definir a função multiplicar(num1, num2) que retorna a multiplicação de dois números.
Definir a função dividir(num1, num2) que retorna a divisão de dois números, verificando antes se o divisor é zero para evitar erro.
Passo 02 - Criar a função principal da calculadora

Utilizar um bloco try-except para capturar entradas inválidas.
Pedir ao usuário para inserir dois números e escolher uma operação (+, -, *, /).
Converter as entradas para float, garantindo que números decimais possam ser usados.
Validar a operação escolhida e chamar a função correspondente.
Se o usuário escolher uma operação inválida, exibir uma mensagem de erro.
Passo 03 - Tratar possíveis erros com try-except

Capturar erros de entrada não numérica (ValueError) e exibir a mensagem: "Erro: Entrada inválida. Digite apenas números."
Capturar a tentativa de divisão por zero (ZeroDivisionError) e exibir a mensagem: "Erro: Divisão por zero não é permitida."
'''
def somar(num1, num2):
    return num1 + num2
 
def subtrair(num1, num2):
    return num1 - num2
 
def multiplicar(num1, num2):
    return num1 * num2
 
def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2
 
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
 
        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida!")
            return
 
        print(f"Resultado: {resultado}")
 
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
 
calculadora()
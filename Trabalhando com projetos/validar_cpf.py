'''
Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir 
com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere 
que não seja um número, o programa deve exibir uma mensagem de erro.

Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

1 - Pedir ao usuário que digite o CPF.
2 - Verificar se tem o formato correto do CPF
3 - Se tiver qualquer outro caractere deve exibir uma mensagem de erro
'''

def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."
 
cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))
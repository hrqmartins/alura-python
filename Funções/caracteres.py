'''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite 
máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
'''

def contar_caracteres(palavra): 
    return len(palavra) 
 
texto = input("Digite uma palavra: ") 
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.") 
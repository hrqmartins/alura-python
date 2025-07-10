'''
Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos.
Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
'''

texto1 = set(input("Texto 1: ").lower().split()) 

texto2 = set(input("Texto 2: ").lower().split()) 

comuns = texto1.intersection(texto2) 

print(f"Palavras em comum: {comuns}") 
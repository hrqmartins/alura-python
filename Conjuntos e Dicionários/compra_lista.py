'''
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

Quais itens apareceram nas duas listas

Quais foram exclusivos de Laura

Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
'''


laura = set(input("Lista da Laura: ").split(", "))  

ana = set(input("Lista da Ana: ").split(", "))  

comuns = laura.intersection(ana)  

exclusivos_laura = laura.difference(ana)  

exlusivos_ana = ana.difference(laura)  

print(f"Itens em ambas as listas: {', '.join(comuns)}")  

print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}")  

print(f"Itens exclusivos de Ana: {', '.join(exlusivos_ana)}") 
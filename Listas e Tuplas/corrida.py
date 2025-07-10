'''
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o 
nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação 
ao final?
'''

resultados = ["Ana", "Carlos", "Pedro"]
print("Lista original:", resultados)

erro = input("Digite o nome incorreto: ")
if erro in resultados:
    correto = input("Digite o nome correto: ")
    posicao = resultados.index(erro)
    resultados.remove(erro)
    resultados.insert(posicao, correto)
    print(f"O nome {erro} foi substituído por {correto}.")
    print("Lista atualizada:", resultados)
else:
    print("Nome não encontrado.")
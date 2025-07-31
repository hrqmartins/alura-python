'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam 
ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja 
encontrada, o programa deve avisar o usuário.
Problema central: O problema central é analisar um texto fornecido pelo usuário, identificar palavras que possuam mais de 10 letras
e exibi-las. Caso não haja palavras longas, o programa deve informar o usuário.

Etapas do processo:

Passo 01 - Receber o texto de entrada

Solicitar que o usuário digite um texto.
Armazenar a entrada em uma variável texto.
Passo 02 - Separar o texto em palavras

Utilizar .split() para dividir o texto em uma lista de palavras, considerando espaços como separadores.
Passo 03 - Identificar palavras longas

Criar uma lista vazia chamada palavras_longas para armazenar palavras com mais de 10 letras.
Percorrer a lista de palavras usando um loop for.
Verificar o comprimento de cada palavra com len(palavra) > 10.
Se a palavra for longa, adicioná-la à lista palavras_longas.
Passo 04 - Exibir o resultado

Se houver palavras na lista palavras_longas, exibi-las uma por linha.
Caso contrário, exibir a mensagem "Nenhuma palavra longa foi encontrada no texto.".
Observação: Caso queira, poderá organizar o código que verifica se a palavra é longa ou não em uma função, por exemplo:
def identificar_palavras_longas(texto).
'''

texto = input("Digite um texto: ")
 
palavras_longas = []
 
for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)
 
if palavras_longas:
    print("Palavras longas encontradas:")
    for palavra in palavras_longas:
        print(palavra)
else:
    print("Nenhuma palavra longa foi encontrada no texto.")
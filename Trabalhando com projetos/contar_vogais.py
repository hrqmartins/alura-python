'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. 
Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

Problema central: O problema central é percorrer um texto fornecido pelo usuário e contar quantas vogais (a, e, i, o, u) ele contém, independentemente de serem maiúsculas ou minúsculas.

Etapas do processo:

Passo 01 - Criar uma função para contar vogais

Definir a função contar_vogais(texto), que receberá o texto como argumento.
Criar uma variável vogais contendo todas as vogais em minúsculas para facilitar a verificação.
Passo 02 - Percorrer o texto e contar as vogais

Converter o texto para minúsculas usando .lower(), garantindo que vogais maiúsculas também sejam contabilizadas.
Inicializar uma variável quantidade para armazenar a contagem das vogais.
Usar um loop for para percorrer cada letra do texto.
Verificar se a letra está na variável vogais e, se estiver, incrementar quantidade.
Passo 03 - Retornar o resultado da contagem

A função contar_vogais() retorna o número total de vogais encontradas no texto.
Passo 04 - Solicitar a entrada do usuário e exibir o resultado

Pedir ao usuário que digite um texto.
Chamar a função contar_vogais() passando o texto informado.
Exibir a contagem formatada na tela.
'''

def contar_vogais(texto):  
    vogais = "aeiou"  
    quantidade = 0  
 
    for letra in texto.lower():  
        if letra in vogais:  
            quantidade += 1  
 
    return quantidade  
 
texto = input("Digite um texto: ") 
 
print(f"O texto contém {contar_vogais(texto)} vogais.")
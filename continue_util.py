'''
Ana está implementando um sistema de filtragem de livros no Buscante. A funcionalidade deve percorrer uma lista de livros e exibir o nome de 
cada livro disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.

Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".
'''

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")
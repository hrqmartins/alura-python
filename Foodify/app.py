import os

restaurantes = ['Outback', 'McDonalds', 'Burger King']  # Lista para armazenar os restaurantes cadastrados

def exibir_nome_do_programa():
    # Menu
    print("""
      
█▀▀ █▀█ █▀█ █▀▄ █ █▀▀ █▄█
█▀░ █▄█ █▄█ █▄▀ █ █▀░ ░█░

      """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair')
    print('-------------------------\n')

# Função para encerrar o aplicativo
def encerrar_app():
    exibir_subtitulo('Encerrando o Foodify...')

def voltar_ao_menu():
    input('Pressione ENTER para voltar ao menu principal...')
    main()

# Função para exibir mensagem de opção inválida
def opcao_invalida():
    print('Opção inválida! Por favor, escolha uma opção válida.')
    voltar_ao_menu()
    
def cadastrar_novo_restaurante():
    os.system('cls')
    exibir_subtitulo('----- Cadastro de Novos Restaurante -----')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)  # Adiciona o restaurante à lista
    print(f'Restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    print('------------------------------------------\n')
    voltar_ao_menu()
    
def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('----- Lista de Restaurantes -----')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    print('---------------------------------\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()

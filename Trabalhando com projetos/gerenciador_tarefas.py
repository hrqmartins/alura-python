'''
Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de
uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para 
armazenar as tarefas.

Problema central: O desafio é criar um programa que permita ao usuário gerenciar tarefas adicionando, visualizando e removendo itens de uma lista. Para isso, o programa precisa exibir um menu interativo e aceitar diferentes entradas do usuário, e tratar essas entradas para evitar erros inesperados. Podemos modularizar a lógica deste desafio em uma função.

Etapas do processo:

Passo 01 - Criar uma lista para armazenar as tarefas

Definir uma lista vazia chamada tarefas para armazenar as tarefas do usuário.
Passo 02 - Criar um menu interativo

Utilizar um loop while para manter o programa rodando até o usuário escolher sair.
Exibir as opções disponíveis no menu:
1: Adicionar uma tarefa.
2: Visualizar a lista de tarefas.
3: Remover uma tarefa da lista.
4: Sair do programa.
Passo 03 - Implementar a funcionalidade de adicionar tarefas

Pedir ao usuário que digite uma nova tarefa.
Validar a entrada para evitar que tarefas vazias sejam adicionadas.
Adicionar a tarefa à lista tarefas.
Exibir a mensagem "Tarefa adicionada!".
Passo 04 - Implementar a funcionalidade de visualizar tarefas

Exibir a lista de tarefas numerada, para facilitar a referência.
Se a lista estiver vazia, exibir "Nenhuma tarefa cadastrada.".
Passo 05 - Implementar a funcionalidade de remover tarefas

Verificar se há tarefas na lista antes de solicitar a remoção.
Pedir ao usuário que digite o número da tarefa a ser removida.
Tratar erros de entrada, garantindo que o usuário digite um número válido.
Se o número for válido, remover a tarefa correspondente e exibir a mensagem "Tarefa removida!".
Se o número for inválido, exibir ** "Erro: Índice inválido!"**.
Passo 06 - Implementar a opção de saída

Se o usuário escolher a opção 4, o programa encerra o loop e exibe "Saindo do gerenciador de tarefas. Até mais!".
'''

def gerenciador_tarefas():
    tarefas = []
 
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:  # Verifica se a string não está vazia
                tarefas.append(tarefa)
                print("Tarefa adicionada!")
            else:
                print("Erro: A tarefa não pode estar vazia.")
 
        elif opcao == "2":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")
 
        elif opcao == "3":
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                continue
 
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Índice inválido! Digite um número válido.")
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")
 
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
 
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
 
gerenciador_tarefas()

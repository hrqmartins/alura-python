'''
Lucas é responsável por um sistema de processamento de dados, onde múltiplas tarefas são executadas ao mesmo tempo. 
No entanto, ele precisa garantir que o sistema seja capaz de monitorar quais tarefas já foram concluídas e quais ainda 
estão em andamento.

Seu objetivo é criar um programa assíncrono que execute três tarefas simultaneamente, simulando um processamento de dados
com tempos diferentes. Existem três tarefas, cada uma com um tempo fixo de execução:

Tarefa 1: 3 segundos.
Tarefa 2: 5 segundos.
Tarefa 3: 7 segundos.
O sistema deve verificar a cada segundo o status de todas as tarefas e exibir quais ainda estão "Em andamento" e quais 
já foram "Finalizadas";
Assim que uma tarefa for concluída, o programa deve exibir uma mensagem informando sua finalização;
O programa só deve terminar quando todas as tarefas forem finalizadas.
'''

import asyncio
 
async def tarefa(numero, tempo):
    await asyncio.sleep(tempo)
    print(f"Tarefa {numero} finalizada!")
 
async def main():
    tempos = [3, 5, 7]
    tarefas = [asyncio.create_task(tarefa(i+1, tempos[i])) for i in range(3)]
 
    while any(not t.done() for t in tarefas):
        status = ['Finalizado' if t.done() else 'Em andamento' for t in tarefas]
        print(f"Status das tarefas: {status}")
        await asyncio.sleep(1) 
 
    await asyncio.gather(*tarefas)
 
asyncio.run(main())
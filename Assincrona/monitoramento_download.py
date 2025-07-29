'''
Imagine que você está desenvolvendo um gerenciador de downloads que permite baixar múltiplos arquivos simultaneamente. 
Como nem todos os arquivos têm o mesmo tamanho, alguns downloads demoram mais que outros. Seu programa deve:

Baixar cinco arquivos diferentes, cada um com um tamanho aleatório entre 10MB e 50MB;
A velocidade de download de cada arquivo é de 5MB por segundo;
Exibir mensagens de progresso a cada segundo, mostrando quanto já foi baixado de cada arquivo;
Exibir uma mensagem quando cada download for concluído;
Aguarde todos os downloads antes de encerrar o programa.
'''

import asyncio

arquivos = {
    "arquivo_1.txt": 30,
    "arquivo_2.txt": 45,
    "arquivo_3.txt": 20,
    "arquivo_4.txt": 10,
    "arquivo_5.txt": 50,
}

VELOCIDADE_DOWNLOAD = 5 

async def baixar_arquivo(nome, tamanho):
    print(f"Iniciando download de {nome} (tamanho: {tamanho}MB)...")
    
    baixado = 0
    segundos = 0
    
    while baixado < tamanho:
        await asyncio.sleep(1)  
        baixado += VELOCIDADE_DOWNLOAD
        baixado = min(baixado, tamanho)
        segundos += 1
        print(f"[{segundos}s] {nome}: {baixado}MB baixados")

    print(f"{nome} concluído!\n")

async def main():
    tarefas = [asyncio.create_task(baixar_arquivo(nome, tamanho)) for nome, tamanho in arquivos.items()]
    await asyncio.gather(*tarefas)
    print("\nTodos os downloads foram finalizados!")

asyncio.run(main())
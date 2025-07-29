'''
Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, algumas notificações 
só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, se o usuário for VIP, ele deve receber 
uma notificação prioritária antes das demais.

Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status 
diferente:

Ana: VIP (deve receber uma notificação prioritária antes das normais).
João: Usuário comum, mas ativou as notificações.
Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.
'''

import asyncio

usuarios = [
    {"nome": "Ana", "vip": True, "notificacoes_ativadas": True},
    {"nome": "João", "vip": False, "notificacoes_ativadas": True},
    {"nome": "Carla", "vip": False, "notificacoes_ativadas": False},
]

async def enviar_notificacao(usuario):
    if not usuario["notificacoes_ativadas"]:
        print(f"{usuario['nome']} desativou as notificações. Nada foi enviado.")
        return
    
    if usuario["vip"]:
        print(f"Notificação VIP para {usuario['nome']} enviada!")
        return
    
    print(f"Notificação normal para {usuario['nome']} enviada!")

async def main():
    print("Enviando notificações...")
    tarefas = [asyncio.create_task(enviar_notificacao(u)) for u in usuarios]
    await asyncio.gather(*tarefas)
    print("Todas as notificações foram processadas!")

asyncio.run(main())
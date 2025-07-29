'''
Paula trabalha em uma plataforma de ensino online e precisa garantir que os alunos sejam inscritos corretamente nos cursos 
desejados. O sistema deve seguir as seguintes regras:

Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso.
A lista de alunos e os cursos disponíveis já está definida no sistema. Lembre-se de processar múltiplas inscrições em paralelo. 
Confira o código:
'''

import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},
]

async def inscrever_aluno(aluno):
    curso_nome = aluno["curso"]
    nome_aluno = aluno["nome"]
    
    print(f"Inscrevendo {nome_aluno} no curso {curso_nome}...")

    if curso_nome not in cursos:
        print(f"Erro! O curso {curso_nome} não existe.\n")
        return

    curso = cursos[curso_nome]

    if nome_aluno in curso["inscritos"]:
        print(f"{nome_aluno} já está inscrito no curso {curso_nome}! Inscrição rejeitada.\n")
        return

    if curso["vagas"] > 0:
        curso["inscritos"].append(nome_aluno)
        curso["vagas"] -= 1
        print(f"Inscrição confirmada para {nome_aluno} no curso {curso_nome}!\n")
    else:
        print(f"Turma lotada! {nome_aluno} não pôde se inscrever no curso {curso_nome}.\n")

async def main():
    tarefas = [asyncio.create_task(inscrever_aluno(a)) for a in alunos]
    await asyncio.gather(*tarefas)
    print("Todas as inscrições foram processadas!\n")

asyncio.run(main())
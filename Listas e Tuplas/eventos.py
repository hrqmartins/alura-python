'''
A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a
sequência dos eventos de uma conferência importante. Os eventos foram registrados na ordem inversa à que deveriam 
acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o
planejamento original.

Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a 
lista final siga a sequência correta.
'''

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

eventos_registrados.reverse()
print(f"Ordem corrigida: {eventos_registrados}")
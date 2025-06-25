'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi 
aprovado ou negado com base nas condições acima.
'''

# Menu
print("------------------------------------------------------------------------")
print("\033[38;5;82m"
    """
      
██████╗░██████╗░░█████╗░████████╗██╗░█████╗░░█████╗░███╗░░██╗██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗
██████╔╝██████╔╝███████║░░░██║░░░██║██║░░╚═╝███████║██╔██╗██║██║░░██║██║░░██║
██╔═══╝░██╔══██╗██╔══██║░░░██║░░░██║██║░░██╗██╔══██║██║╚████║██║░░██║██║░░██║
██║░░░░░██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░░██║██║░╚███║██████╔╝╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝

      """
       "\033[0m")

print("------------------------------------------------------------------------\n")

# Solicita a renda mensal e o valor da parcela
renda_mensal = float(input("Digite a renda mensal: R$ "))
valor_parcela = float(input("Digite o valor da parcela desejada: R$ "))

# Calculo
if renda_mensal > 2000 and valor_parcela <= 0.3 * renda_mensal:
    print("Empréstimo aprovado!")
elif renda_mensal <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")
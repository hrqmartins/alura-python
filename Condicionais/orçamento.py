'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de
um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite
ou ainda está dentro do orçamento.
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

# Solicita o total de despesas realizadas
total_despesas = float(input("Digite o total de despesas realizadas R$: "))

# Verifica se ultrapassou o limite
if total_despesas > 3000:
    print("Você ultrapassou o limite do orçamento!")
else:
    print("Você está dentro do orçamento.")
    
    
    
# GABARITO DO INSTRUTOR
# limite = 3000.0
# despesas = float(input("Digite o total de despesas do mês (R$): "))

# if despesas > limite:
#     print("Atenção! Você ultrapassou o limite do orçamento.")
# else:
#     print("Você está dentro do orçamento.")
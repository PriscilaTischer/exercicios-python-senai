# Exercício 8: Informe o nome do mês correspondente a um número.

print("--- MÊS POR EXTENSO ---")

numero_mes = int(input("Digite o número do mês (1 a 12): "))
if numero_mes == 1:
    print("O mês é Janeiro.")
elif numero_mes == 2:
    print("O mês é Fevereiro.")
elif numero_mes == 3:
    print("O mês é Março.")
elif numero_mes == 4:
    print("O mês é Abril.")
elif numero_mes == 5:
    print("O mês é Maio.")
elif numero_mes == 6:
    print("O mês é Junho.")
elif numero_mes == 7:
    print("O mês é Julho.")
elif numero_mes == 8:
    print("O mês é Agosto.")
elif numero_mes == 9:
    print("O mês é Setembro.")
elif numero_mes == 10:
    print("O mês é Outubro.")
elif numero_mes == 11:
    print("O mês é Novembro.")
elif numero_mes == 12:
    print("O mês é Dezembro.")
else:
    print("Erro: Não existe um mês com este número. Por favor, digite um valor entre 1 e 12.")
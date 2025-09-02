# Exercício 4: Simulador de aprovação de empréstimo imobiliário.

print("--- SIMULADOR DE EMPRÉSTIMO BANCÁRIO ---")

valor_casa = float(input("Qual o valor da casa que deseja comprar? R$ "))
salario = float(input("Qual é o seu salário mensal? R$ "))
anos_pagamento = int(input("Em quantos anos você pretende pagar? "))
numero_meses = anos_pagamento * 12
prestacao_mensal = valor_casa / numero_meses
limite_prestacao = salario * 0.30

print(f"\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos_pagamento} anos,")
print(f"a prestação mensal será de R$ {prestacao_mensal:.2f}.")
print(f"O valor máximo de prestação que você pode pagar é de R$ {limite_prestacao:.2f} (30% do seu salário).")
if prestacao_mensal <= limite_prestacao:
    print("\nParabéns! Empréstimo APROVADO.")
else:
    print("\nInfelizmente, seu empréstimo foi NEGADO, pois a prestação excede 30% do seu salário.")
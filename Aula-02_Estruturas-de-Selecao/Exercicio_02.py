# Exercício 2: Calcular o aumento de salário com base em faixas.

print("--- CÁLCULO DE AUMENTO SALARIAL ---")

salario_atual = float(input("Digite o valor do salário do funcionário: R$ "))
if salario_atual > 1250.00:
    percentual_aumento = 10
else:
    percentual_aumento = 15
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print(f"\nO salário de R$ {salario_atual:.2f} receberá um aumento de {percentual_aumento}%.")
print(f"O valor do aumento é de R$ {valor_aumento:.2f}.")
print(f"O novo salário será de R$ {novo_salario:.2f}.")
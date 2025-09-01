# Exercício 3: Calcule o aumento de um salário.

print("--- CALCULADORA DE AUMENTO SALARIAL ---")

salario_atual = float(input("Digite o valor do salário atual: R$ "))
percentual_aumento = float(input("Digite a porcentagem de aumento (%): "))
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

#os resultados
print("\n--- RESULTADO ---")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
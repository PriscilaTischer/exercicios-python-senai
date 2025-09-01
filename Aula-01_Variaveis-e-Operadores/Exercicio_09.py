# Exercício 9: Calcule o peso ideal para homens e mulheres.

print("--- CALCULADORA DE PESO IDEAL ---")

altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(f"\nPara a altura de {altura}m:")
print(f"O peso ideal para um homem é: {peso_ideal_homem:.2f} kg")
print(f"O peso ideal para uma mulher é: {peso_ideal_mulher:.2f} kg")
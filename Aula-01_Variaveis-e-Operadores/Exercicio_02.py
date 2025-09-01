# Exercício 2: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

print("--- CONVERSOR DE METROS PARA MILÍMETROS ---")
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros} metros equivalem a {milimetros:.0f} milímetros.")
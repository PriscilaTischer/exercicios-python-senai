# Exercício 6: Apresente o antecessor e o sucessor de um número.

print("--- ANTECESSOR E SUCESSOR ---")

numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"\nAnalisando o número {numero}:")
print(f"Seu antecessor é: {antecessor}")
print(f"Seu sucessor é: {sucessor}")
# Exercício 6: Verifique se um número é par ou ímpar.

print("--- PAR OU ÍMPAR ---")
numero = int(input("Digite um número inteiro: "))
if (numero % 2) == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
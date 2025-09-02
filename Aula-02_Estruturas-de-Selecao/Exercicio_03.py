# Exercício 3: Criar uma calculadora para as 4 operações básicas.

print("--- CALCULADORA SIMPLES ---")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("(+) para Soma")
print("(-) para Subtração")
print("(*) para Multiplicação")
print("(/) para Divisão")
operacao = input("Qual operação deseja realizar? ")
if operacao == '+':
    resultado = num1 + num2
    print(f"\nO resultado de {num1} + {num2} é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"\nO resultado de {num1} - {num2} é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"\nO resultado de {num1} * {num2} é: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nO resultado de {num1} / {num2} é: {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero.")
else:
    print("\nOperação inválida. Por favor, escolha +, -, * ou /.")
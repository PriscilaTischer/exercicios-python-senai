# Exercício 9: Calcule a raiz quadrada para positivos e o quadrado para negativos.
import math # Importa a biblioteca de matemática para usar a função de raiz quadrada

print("--- RAIZ QUADRADA OU QUADRADO ---")
numero = float(input("Digite um número qualquer: "))


if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"O número é positivo. A raiz quadrada de {numero} é {raiz:.2f}.")
else:
    quadrado = numero ** 2
    print(f"O número é negativo. O quadrado de {numero} é {quadrado:.2f}.")
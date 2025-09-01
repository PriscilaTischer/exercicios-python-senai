# Exercício 5: Converta uma temperatura de Celsius para Fahrenheit.

print("--- CONVERSOR DE TEMPERATURA (°C -> °F) ---")

#temperatura em Celsius
celsius = float(input("Digite a temperatura em Graus Celsius (°C): "))

#para Fahrenheit (F = (C * 9/5) + 32)
fahrenheit = (celsius * 9/5) + 32

#resultado
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F.")
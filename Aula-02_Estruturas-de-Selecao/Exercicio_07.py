# Exercício 7: Verifique se uma pessoa está apta a doar sangue.

print("--- REQUISITOS PARA DOAÇÃO DE SANGUE ---")

idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso (em kg)? "))
horas_sono = int(input("Quantas horas você dormiu nas últimas 24h? "))

if (idade >= 16 and idade <= 69) and (peso > 50) and (horas_sono >= 6):
    print("\nParabéns! Você atende aos requisitos para doar sangue.")
else:
    print("\nInfelizmente, você não atende a todos os requisitos para doar sangue no momento.")
    print("Requisitos: ter entre 16 e 69 anos, pesar mais de 50kg e ter dormido pelo menos 6h.")
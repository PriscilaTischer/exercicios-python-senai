# Exercício 1: Calcular a multa de trânsito.

print("--- RADAR DE VELOCIDADE ---")

velocidade = float(input("Digite a velocidade do carro (em km/h): "))
LIMITE_VELOCIDADE = 80.0
VALOR_MULTA_POR_KM = 5.00

if velocidade > LIMITE_VELOCIDADE:
    km_acima = velocidade - LIMITE_VELOCIDADE
    multa = km_acima * VALOR_MULTA_POR_KM

    print("\nMULTADO! Você excedeu o limite de velocidade de 80 km/h.")
    print(f"Você estava a {velocidade} km/h, {km_acima:.1f} km/h acima do permitido.")
    print(f"O valor da sua multa é de R$ {multa:.2f}.")
else:
    print("\nVelocidade dentro do permitido. Boa viagem!")
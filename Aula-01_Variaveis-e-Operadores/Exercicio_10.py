# Exercício 10: Calcule a multa por excesso de peso de pesca.

print("--- CONTROLE DE PESCA ---")
LIMITE_PESO_KG = 50.0
VALOR_MULTA_POR_KG = 4.0
peso_peixes = float(input("Digite o peso de peixes (kg): "))
if peso_peixes > LIMITE_PESO_KG:
    excesso = peso_peixes - LIMITE_PESO_KG
    multa = excesso * VALOR_MULTA_POR_KG
    print("\nPesca com peso acima do regulamento!")
    print(f"Peso excedente: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("\nPesca dentro do regulamento. Não há multa a pagar.")
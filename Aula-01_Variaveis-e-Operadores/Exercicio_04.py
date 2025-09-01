#Exercício 4: Calcule o desconto sobre uma mercadoria.

print("--- CALCULADORA DE DESCONTO ---")

preco_mercadoria = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))
valor_desconto = preco_mercadoria * (percentual_desconto / 100)
preco_a_pagar = preco_mercadoria - valor_desconto

#resultados
print("\n--- RESULTADO ---")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
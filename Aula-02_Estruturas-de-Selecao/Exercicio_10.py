# Exercício 10: Sugira a forma de pagamento com base no valor da compra.

print("--- SUGESTÃO DE PAGAMENTO ---")

valor_compra = float(input("Digite o valor total da compra: R$ "))
if valor_compra <= 100.00:
    print("Para este valor, a forma de pagamento sugerida é: Dinheiro.")
elif valor_compra > 100.00 and valor_compra <= 300.00:
    print("Para este valor, a forma de pagamento sugerida é: Cartão de Débito.")
else: 
    print("Para este valor, a forma de pagamento sugerida é: Cartão de Crédito.")
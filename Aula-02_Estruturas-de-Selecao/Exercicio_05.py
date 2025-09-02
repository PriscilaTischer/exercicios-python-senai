# Exercício 5: Calcular o valor da conta de energia elétrica.

print("--- CÁLCULO DA CONTA DE ENERGIA ---")

kwh_consumidos = float(input("Digite a quantidade de kWh consumidos: "))
print("\nTipo de Instalação:")
print("(R) para Residencial")
print("(C) para Comercial")
print("(I) para Industrial")
tipo_instalacao = input("Qual o tipo de instalação? ").upper() 

preco_a_pagar = 0
invalido = False
if tipo_instalacao == 'R':
    if kwh_consumidos <= 500:
        preco_a_pagar = kwh_consumidos * 0.40
    else:
        preco_a_pagar = kwh_consumidos * 0.65
elif tipo_instalacao == 'C':
    if kwh_consumidos <= 1000:
        preco_a_pagar = kwh_consumidos * 0.55
    else:
        preco_a_pagar = kwh_consumidos * 0.60
elif tipo_instalacao == 'I':
    if kwh_consumidos <= 5000:
        preco_a_pagar = kwh_consumidos * 0.55
    else:
        preco_a_pagar = kwh_consumidos * 0.60
else:
    invalido = True
    print("\nErro: Tipo de instalação inválido. Por favor, digite R, C ou I.")
if not invalido:
    print(f"\nO valor a pagar pela sua conta de energia é: R$ {preco_a_pagar:.2f}")
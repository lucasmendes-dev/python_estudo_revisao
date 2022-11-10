###----- Treinando loop for e condicionais -----###

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

"""for i, venda in enumerate(vendas):
    for c, vendedor in enumerate(vendedores):
        if(c == i):
            print(f"O vendedor {vendedor} vendeu {venda}")"""

for i in range(len(vendas)):
    print(f"O Vendedor {vendedores[i]} vendeu {vendas[i]}")

media = sum(vendas) / len(vendas)
print(f"A média de vendas foi de {media}")
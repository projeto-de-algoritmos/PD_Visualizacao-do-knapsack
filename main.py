def knapsack(peso_max, pesos, valores, n):
    table = [[0 for _ in range(peso_max + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for peso_atual in range(peso_max + 1):
            if i == 0 or peso_atual == 0:
                table[i][peso_atual] = 0
            elif pesos[i - 1] <= peso_atual:
                table[i][peso_atual] = max(valores[i - 1] + table[i - 1][peso_atual - pesos[i - 1]], table[i - 1][peso_atual])
            else:
                table[i][peso_atual] = table[i - 1][peso_atual]
    
    return table[n][peso_max]

valores = []
pesos = []

peso_max = int(input("Digite o peso máximo da sua mochila: "))
n = int(input("Digite o número de itens a serem processados: "))

for i in range(n):
    print(i + 1)
    valor_item = int(input("Digite o valor do item: "))
    peso_item = int(input("Digite o peso do item: "))
    valores.append(valor_item)
    pesos.append(peso_item)

print("Valor máximo obtido:", knapsack(peso_max, pesos, valores, n))

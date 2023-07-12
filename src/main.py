from knapsack import Knapsack


if (__name__ == "__main__"):

    knapsack = Knapsack()
    knapsack.set()
    max_valor, itens_escolhidos = knapsack.knapsack()
    table = knapsack.get_table()

    # Imprimir a tabela
    for row in table:
        print(row)

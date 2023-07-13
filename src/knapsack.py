class Knapsack:
    def __init__(self):
        self.valores = []
        self.pesos = []
        self.peso_max = 0
        self.quantiaItens = 0
        self.table = []

    def set(self):
        self.peso_max = int(input("Digite o peso máximo da sua mochila: "))
        self.quantiaItens = int(
            input("Digite o número de itens a serem processados: "))

        for i in range(self.quantiaItens):
            valor_item = int(input(f"Digite o valor do item {i + 1}: "))
            peso_item = int(input(f"Digite o peso do item {i + 1}: "))
            self.valores.append(valor_item)
            self.pesos.append(peso_item)

    def knapsack(self):
        self.table = [[0 for _ in range(self.peso_max + 1)] for _ in range(self.quantiaItens + 1)]
        list_itens_escolhidos = []

        for i in range(1, self.quantiaItens + 1):
            for j in range(1, self.peso_max + 1):
                if self.pesos[i - 1] <= j:
                    self.table[i][j] = max(self.valores[i - 1] + self.table[i - 1][j - self.pesos[i - 1]], self.table[i - 1][j])
                else:
                    self.table[i][j] = self.table[i - 1][j]

        for i in range(1, self.quantiaItens + 1):
            itens_escolhidos = self.rastreiaItens(i)
            list_itens_escolhidos.append(itens_escolhidos)

        return self.table[self.quantiaItens][self.peso_max], list_itens_escolhidos

    def rastreiaItens(self, linha):
        itens_escolhidos = []
        i = linha
        j = self.peso_max
        while i > 0 and j > 0:
            if self.table[i][j] != self.table[i - 1][j]:
                itens_escolhidos.append(i)
                j -= self.pesos[i - 1]
            i -= 1
        itens_escolhidos.reverse()
        return itens_escolhidos


    def get_table(self):
        return self.table
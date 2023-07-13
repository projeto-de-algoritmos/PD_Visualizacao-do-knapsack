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
            print(i + 1)
            valor_item = int(input("Digite o valor do item: "))
            peso_item = int(input("Digite o peso do item: "))
            self.valores.append(valor_item)
            self.pesos.append(peso_item)

    def knapsack(self):
        self.table = [
            [0 for _ in range(self.peso_max + 1)]
            for _ in range(self.quantiaItens + 1)
        ]

        list_itens_escolhidos = []

        for i in range(self.quantiaItens + 1):
            itens_escolhidos = []
            for peso_atual in range(self.peso_max + 1):
                self.rastreiaItens(itens_escolhidos)

                if i == 0 or peso_atual == 0:
                    self.table[i][peso_atual] = 0
                elif self.pesos[i - 1] <= peso_atual:
                    self.table[i][peso_atual] = max(
                        self.valores[i - 1] + self.table[i - 1][peso_atual - self.pesos[i - 1]], self.table[i - 1][peso_atual])
                else:
                    self.table[i][peso_atual] = self.table[i - 1][peso_atual]
            list_itens_escolhidos.append(self.filter(itens_escolhidos))
            itens_escolhidos=[]


        return self.table[self.quantiaItens][self.peso_max], list_itens_escolhidos


    def filter(self,lista):
        aux=[]
        for item in lista:
            if item not in aux:
                aux.append(item)
        return aux

    def rastreiaItens(self, itens_escolhidos):
        i = self.quantiaItens
        peso_atual = self.peso_max
        while i > 0 and peso_atual > 0:
            if self.table[i][peso_atual] != self.table[i - 1][peso_atual]:
                itens_escolhidos.append(i)
                peso_atual -= self.pesos[i - 1]
            i -= 1

    def get_table(self):
        return self.table

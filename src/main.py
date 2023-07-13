from knapsack import Knapsack
import pyxel


class App:
    def __init__(self, itens):

        self.itens = itens
        self.i = 0

        pyxel.init(150, 150, fps=5)

        pyxel.run(self.update, self.draw)

    def draw(self):
        
        for j in range(self.i):
            y = 3
            x = 20
            for index in self.itens[j]:
                pyxel.rect(x, y+(8*j), 4, 4,index+1)
                x = x + 8
            x = 20

    def update(self):
        if (self.i < len(self.itens)):
            self.i = self.i+1


if (__name__ == "__main__"):

    knapsack = Knapsack()
    knapsack.set()
    max_valor, itens_escolhidos = knapsack.knapsack()
    table = knapsack.get_table()

    # Imprimir a tabela
    for row in itens_escolhidos:
        print(row)

    App(itens_escolhidos)

    # print(itens_escolhidos)

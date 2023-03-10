# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd

# porta avioes: 1x5
# Couraçado: 2x4
# Cruzador: 2x3
# Submarino 2x3
# Destruidor: 3x2

fleet = {'Porta Avioes': 5,
         'Couracado #1': 4,
         'Couracado #2': 4,
         'Cruzador #1': 3,
         'Cruzador #2': 3,
         'Cruzador #3': 3,
         'Submarino #1': 3,
         'Submarino #2': 3,
         'Destruidor #1': 2,
         'Destruidor #2': 2,
         'Destruidor #3': 2}



class board:
    def __init__(self):
        self.tabuleiro = self.board_reset()
        self.frota = fleet.copy()

        self.coords = {'Porta Avioes': [],
                       'Couracado #1': [],
                       'Couracado #2': [],
                       'Cruzador #1': [],
                       'Cruzador #2': [],
                       'Cruzador #3': [],
                       'Submarino #1': [],
                       'Submarino #2': [],
                       'Destruidor #1': [],
                       'Destruidor #2': [],
                       'Destruidor #3': []}

        self.grid_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.grid_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        for key, value in self.frota.items():
            x = np.random.choice(self.grid_x)
            y = np.random.choice(self.grid_y)

            x_pos = self.grid_x.index(x)
            y_pos = self.grid_y.index(y)

            # orientado para E
            if all([x_pos+value <= 9,
                   self.tabuleiro[x_pos][y_pos] == '0',
                   self.tabuleiro[x_pos][y_pos] == '0',
                   self.tabuleiro[x_pos][y_pos] == '0',
                   self.tabuleiro[x_pos][y_pos] == '0']):
                self.coords.update(key,[str(x) + str(y_range) for y_range in range(y_pos+value)])
                construtor = 0
                while construtor <= self.frota.values[key]:
                    construtor += 1
                    self.tabuleiro[x_pos+construtor][y_pos] = "■"
            else:
                self.board_reset()

    def board_reset(self):
        self.tabuleiro = pd.DataFrame(np.zeros(shape=(10, 10), dtype='object'),
                                      columns=list('ABCDEFGHIJ'))
        return self.tabuleiro










class player:
    pass


teste = board()

print(teste.tabuleiro)
teste.tabuleiro['A'][2] = '■'
print(teste.tabuleiro)
print(teste.coords)
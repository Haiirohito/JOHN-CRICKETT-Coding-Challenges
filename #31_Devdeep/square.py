import matplotlib.pyplot as plt
import numpy as np

class Square:
    def __init__(self, ax, side, pos, color):
        self.side = side
        self.pos = pos
        self.color = color
        self.ax = ax

    def draw(self):
        outer_square = plt.Rectangle((self.pos[0], self.pos[1]), self.side, self.side, edgecolor='none', facecolor=self.color)
        self.ax.add_patch(outer_square)

        inner_side = self.side - 2
        white_space = plt.Rectangle((self.pos[0] + 1, self.pos[1] + 1), inner_side, inner_side, edgecolor='none', facecolor='white')
        center_square = plt.Rectangle((self.pos[0] + 2, self.pos[1] + 2), inner_side-2, inner_side-2, edgecolor = 'none', facecolor=self.color)
        self.ax.add_patch(white_space)
        self.ax.add_patch(center_square)

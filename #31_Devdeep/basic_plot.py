import numpy as np
import matplotlib.pyplot as plt

from square import Square

class BasicPlot:
    def __init__(self, size=8, show=True) -> None:
        self.size = size
        self.show = show

    def plot(self, a):
        fig = plt.figure(figsize=(self.size, self.size))
        ax = fig.add_subplot(1, 1, 1)

        interval = np.arange(0, a + 1, 1)

        ax.set_xticks(interval)
        ax.set_yticks(interval)
        ax.grid(color='k', linestyle='--', linewidth=0.5)
        
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)

# makeing the  recognition squares
        # Plot a square with an inner square in the top-left corner
        square1 = Square(ax, 7, (0, 0), 'k')
        square1.draw()
        # Plot a square with an inner square in the bottom-left corner
        square2 = Square(ax, 7, (0, a-7), 'k')
        square2.draw()
        # Plot a square with an inner square in the top-right corner
        square3 = Square(ax, 7, (a-7, a-7), 'k')
        square3.draw()
        
# making the orientation squares


        if self.show:
            plt.show()

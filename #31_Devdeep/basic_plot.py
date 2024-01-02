import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class BasicPlot:
    def __init__(self, size=8, show=True) -> None:
        self.size = size
        self.show = show

    def plot(self, a, n):
        fig = plt.figure(figsize=(self.size, self.size))
        ax = fig.add_subplot(1, 1, 1)

        interval = np.arange(0, a + 1, 1)

        ax.set_xticks(interval)
        ax.set_yticks(interval)
        ax.grid(color='k', linestyle='--', linewidth=0.5)

        # Plot a square in the top-left corner
        top_left_square = plt.Rectangle((0, 0), n, n, edgecolor='r', facecolor='r')
        ax.add_patch(top_left_square)

        # Plot a square in the bottom-left corner
        bottom_left_square = plt.Rectangle((0, a-a//3), n, n, edgecolor='b', facecolor='b')
        ax.add_patch(bottom_left_square)
        
        # Plot a square in the top-right corner
        bottom_left_square = plt.Rectangle((a-a//3, a-a//3), n, n, edgecolor='g', facecolor='g')
        ax.add_patch(bottom_left_square)

        if self.show:
            plt.show()

if __name__ == "__main__":
    # Example usage
    plotter = BasicPlot()
    plotter.plot(22, 7)

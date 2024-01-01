import numpy as np
from matplotlib import pyplot as plt

class basic_plot():
    
    square_side = 1.0

    def __init__(self, size=8, ticks=22) -> None:
        self.size = size
        self.ticks = ticks
        
        
    def add_square(self, x, y, size, ax):
        ax.add_patch(plt.Rectangle((x, y), size, size, color='black'))


    def corner_pattern(self, ax):
        width = self.ticks // 3 - 1
        
        x_bottom_left = [0, width, width, 0]
        y_bottom_left = [0, 0, width, width]
        
        x_top_left = [0, 0, width, width]
        y_top_left = [self.ticks - width - 1, self.ticks - 1, self.ticks - width - 1, self.ticks - 1]
        
        x_top_right = [self.ticks - width - 1, self.ticks - 1, self.ticks - width - 1, self.ticks - 1]
        y_top_right = [self.ticks - width - 1, self.ticks - 1, self.ticks - 1, self.ticks - width - 1]
        
        for i in range(4):
            # Bottom-left square
            self.add_square(x_bottom_left[i], y_bottom_left[i], self.square_side, ax)
            # Top-left square
            self.add_square(x_top_left[i], y_top_left[i] - 1, self.square_side, ax)
            # # Top-right square
            self.add_square(x_top_right[i] - 1, y_top_right[i] - 1, self.square_side, ax)
            

    def plot_grid(self, show=False, qr=False):
        fig = plt.figure(figsize=(self.size, self.size))
        ax = fig.add_subplot(1, 1, 1)

        interval = np.arange(0, self.ticks, 1)

        ax.set_xticks(interval)
        ax.set_yticks(interval)
        ax.grid(color='k', linestyle='--', linewidth=0.5)
        
        # plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False) 

        if qr:
            self.corner_pattern(ax)

        if show:
            plt.show()

ploter = basic_plot(size=8, ticks = 22)
ploter.plot_grid(show=True, qr=True)


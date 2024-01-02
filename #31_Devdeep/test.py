import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class BasicPlot:
    def __init__(self, size=8, show=True) -> None:
        self.size = size
        self.show = show

    def draw_rectangle(self, ax, position, n, color, inner_n, inner_color='white'):
        # Draw outer rectangle
        rectangle = patches.Rectangle(position, n, n, linewidth=1, edgecolor=color, facecolor=color)
        ax.add_patch(rectangle)

        # Calculate inner rectangle position and size
        inner_position = (position[0] + (n - inner_n) / 2, position[1] + (n - inner_n) / 2)
        inner_size = inner_n

        # Draw inner rectangle
        inner_rectangle = patches.Rectangle(inner_position, inner_size, inner_size, facecolor=inner_color)
        ax.add_patch(inner_rectangle)

        # Calculate the center of the inner rectangle
        center_x = inner_position[0] + n / 2
        center_y = inner_position[1] + n / 2

        # Draw a small square in the center with the same color as the outer square
        center_square_size = n-2  # Ensure the center square is fully contained within the central region
        center_square = patches.Rectangle((center_x - center_square_size / 2, center_y - center_square_size / 2),
                                          center_square_size, center_square_size, facecolor=color)
        ax.add_patch(center_square)

    def plot(self, a, n, inner_n):
        fig = plt.figure(figsize=(self.size, self.size))
        ax = fig.add_subplot(1, 1, 1)

        interval = np.arange(0, a + 1, 1)

        ax.set_xticks(interval)
        ax.set_yticks(interval)
        ax.grid(color='k', linestyle='--', linewidth=0.5)

        # Plot a square with an inner square in the top-left corner
        self.draw_rectangle(ax, (0, 0), n, 'k', inner_n)

        # Plot a square with an inner square in the bottom-left corner
        self.draw_rectangle(ax, (0, a - a//3), n, 'k', inner_n)

        # Plot a square with an inner square in the top-right corner
        self.draw_rectangle(ax, (a - a//3, a - a//3), n, 'k', inner_n)

        if self.show:
            plt.show()

if __name__ == "__main__":
    # Example usage
    plotter = BasicPlot()
    plotter.plot(22, 7, 5)

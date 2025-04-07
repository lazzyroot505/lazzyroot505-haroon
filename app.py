import matplotlib.pyplot as plt
import numpy as np

def draw_shapes():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Circle
    circle = plt.Circle((0.2, 0.5), 0.1, edgecolor='cyan', facecolor='none', linewidth=2)
    ax.add_patch(circle)

    # Square
    square = plt.Rectangle((0.4, 0.4), 0.2, 0.2, edgecolor='magenta', facecolor='none', linewidth=2)
    ax.add_patch(square)

    # Triangle
    triangle = plt.Polygon(np.array([[0.7, 0.4], [0.8, 0.6], [0.9, 0.4]]), edgecolor='yellow', facecolor='none', linewidth=2)
    ax.add_patch(triangle)

    # Rectangle
    rectangle = plt.Rectangle((0.6, 0.6), 0.3, 0.1, edgecolor='lime', facecolor='none', linewidth=2)
    ax.add_patch(rectangle)

    plt.axis('off')
    plt.savefig('shapes.svg')

if __name__ == "__main__":
    draw_shapes()

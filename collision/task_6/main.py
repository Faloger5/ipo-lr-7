import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_rectangles(rects):
    fig, ax = plt.subplots()
    for rect in rects:
        (x_min, y_min), (x_max, y_max) = rect
        width = x_max - x_min
        height = y_max - y_min
        rect_patch = patches.Rectangle((x_min, y_min), width, height, fill=False)
        ax.add_patch(rect_patch)
    ax.set_aspect('equal')
    plt.show()

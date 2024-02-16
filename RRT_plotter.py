from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

custom_color = "#4E2A84"  
custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "custom_cmap", [(0, custom_color), (1, "white")]
)


class Plotter:

    def __init__(self, rrt):
        self.rrt = rrt

        # Calculate the figure size to match the image dimensions
        fig_width = rrt.image.shape[1] / 100  # Assuming 100 pixels per unit
        fig_height = rrt.image.shape[0] / 100  # Assuming 100 pixels per unit

        self.fig, self.ax = plt.subplots(figsize=(fig_width, fig_height))
        
        # Plot the image first
        self.ax.imshow(1 - self.rrt.image, cmap=custom_cmap, origin='lower')
        self.ax.set_xlim(0, self.rrt.D[0])
        self.ax.set_ylim(0, self.rrt.D[1])
        self.ax.set_aspect('equal')

        # Hide axis numbers, labels, and ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        # Elements to be animated
        self.edges = LineCollection([], linewidths=(0.75), colors='dimgray', linestyle='solid')
        self.ax.add_collection(self.edges)
        self.vertices, = self.ax.plot([], [], color='dimgray', marker='o', linestyle='None', markersize=1.1)
        self.path_line, = self.ax.plot([], [], 'green', linewidth=4.5)

        # Plot static elements
        self.plot_start_and_goal()
        self.plot_circle_obstacles()

        # Animation control
        self.animation_running = True
        self.path_plotted = False

    def plot_start_and_goal(self):
        self.ax.plot(self.rrt.q_init[0], self.rrt.q_init[1], 'ro', markersize=7)  
        self.ax.plot(self.rrt.q_goal[0], self.rrt.q_goal[1], 'rx', markersize=10)  

    def plot_circle_obstacles(self): 
        for crc in self.rrt.circle_obstacles:
            circle = plt.Circle((crc[0], crc[1]), crc[2], color='black')
            self.ax.add_patch(circle)

    def update(self, i):
        if not self.animation_running:
            return self.vertices, self.edges, self.path_line

        # gather vertices and edges up to frame i
        vertices = np.array(list(self.rrt.G.keys())[:i+1])
        edge_segments = []
        for v, neighbors in list(self.rrt.G.items())[:i+1]:
            for n in neighbors:
                edge_segments.append([v, n])

        # update vertices and edges for the current frame
        self.vertices.set_data(vertices[:, 0], vertices[:, 1])
        self.edges.set_segments(edge_segments)

        # Check if the path is found and animate it
        if self.rrt.path and not self.path_plotted:
            path_length = len(self.rrt.path)
            path_index = min(i - len(self.rrt.G) + path_length, path_length)
            if path_index > 0:
                x_coords, y_coords = zip(*self.rrt.path[:path_index])
                self.path_line.set_data(x_coords, y_coords)

            if path_index == path_length:
                self.path_plotted = True
                self.animation_running = False  # stop the animation

        return self.vertices, self.edges, self.path_line

    def animate(self):
        total_frames = len(self.rrt.G) + len(self.rrt.path) if self.rrt.path else len(self.rrt.G)
        anim = FuncAnimation(self.fig, self.update, frames=total_frames, interval=5, blit=True)
        plt.show()

    def show(self):
        self.animate()

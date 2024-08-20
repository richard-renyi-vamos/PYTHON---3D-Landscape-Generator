import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from noise import pnoise2

class Landscape3D:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Landscape Generator")

        # Set up the frame for the controls
        self.controls_frame = ttk.Frame(root)
        self.controls_frame.pack(side=tk.TOP, fill=tk.X)

        # Size input
        ttk.Label(self.controls_frame, text="Size:").pack(side=tk.LEFT)
        self.size_var = tk.IntVar(value=100)
        ttk.Entry(self.controls_frame, textvariable=self.size_var, width=5).pack(side=tk.LEFT)

        # Scale input
        ttk.Label(self.controls_frame, text="Scale:").pack(side=tk.LEFT)
        self.scale_var = tk.DoubleVar(value=30.0)
        ttk.Entry(self.controls_frame, textvariable=self.scale_var, width=5).pack(side=tk.LEFT)

        # Generate Button
        self.generate_button = ttk.Button(self.controls_frame, text="Generate Landscape", command=self.generate_landscape)
        self.generate_button.pack(side=tk.LEFT, padx=10)

    def generate_landscape(self):
        size = self.size_var.get()
        scale = self.scale_var.get()

        x = np.linspace(-5, 5, size)
        y = np.linspace(-5, 5, size)
        x, y = np.meshgrid(x, y)

        z = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                z[i][j] = pnoise2(x[i][j] / scale, y[i][j] / scale)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='terrain')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    landscape_app = Landscape3D(root)
    root.mainloop()

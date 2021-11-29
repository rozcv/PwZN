from PIL import Image, ImageDraw
import random
import numpy as np


class simulationIsing:
    def __init__(self, size, J, B, H, steps, density, file):
        self.size = size
        self.J = J
        self.B = B
        self.H = H
        self.steps = steps
        self.density = density  # none
        self.file = file
        self.nbSpins = size * size
        self.table = np.random.randint(0, 2, (self.size, self.size))  # 0 or 1

        print(self.table)

    def image(self):
        image = Image.new('RGB', (self.size, self.size), color=(253, 194, 0))

        for i in range(self.size):
            for j in range(self.size):
                if i < len(self.table):
                    if self.table[i, j] == 1:
                        image.putpixel((i, j), (0, 0, 0))
                    else:
                        image.putpixel((i, j), (255, 255, 255))
                else:
                    StopIteration()

        image.save("image.png")

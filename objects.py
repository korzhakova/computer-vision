import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load('Desktop/study/3/computer-vision/img/ps.npy.txt')

print("Общее количество объектов: ", np.max(label(image)))

rect = np.ones((4, 6))
rect_image = binary_erosion(image, rect)
rect_count = np.max(label(rect_image))
print(rect_count)

figure = np.array([[1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1]])

figure_image = binary_erosion(image, figure)
print(np.max(label(figure_image)) - rect_count)


figure = np.array([[1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]])

figure_image = binary_erosion(image, figure)
print(np.max(label(figure_image)) - rect_count)


figure = np.array([[1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [0, 0, 1, 1],
                   [0, 0, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1]])

figure_image = binary_erosion(image, figure)
print(np.max(label(figure_image)))


figure = np.array([[1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1]])

figure_image = binary_erosion(image, figure)
print(np.max(label(figure_image)))
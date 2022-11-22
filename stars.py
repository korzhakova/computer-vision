import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load("Desktop/study/3/computer-vision/img/stars.npy")



plus = np.array([   [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]])

star = np.array([   [1, 0, 0, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [1, 0, 0, 0, 1]])

stars_image = binary_erosion(image, plus)
stars_count = np.max(label(stars_image))

stars_image = binary_erosion(image, star)
stars_count += np.max(label(stars_image))


print("Количество звездочек: ", stars_count)
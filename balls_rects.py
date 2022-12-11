import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from skimage.measure import label, regionprops
from skimage import color

def count(colors):
    keys = sorted(colors.keys())
    diff = np.diff(keys)
    delta = np.std(diff) * 2
    
    for i in range(1, len(keys)):
        k1 = keys[i]
        k2 = keys[i-1]   
        if(delta >= k1 - k2):
            colors[k1] += colors[k2]
            colors.pop(k2, 0)      
    return colors

image = plt.imread('Desktop/study/3/computer-vision/img/balls_and_rects.png')
hsv = color.rgb2hsv(image)

binary = np.mean(hsv, 2)
binary[binary > 0] = 1

labeled = label(binary)

print("Objects: ", labeled.max())

regions = regionprops(labeled)

circles = defaultdict(lambda: 0)
rects = defaultdict(lambda: 0)

for region in regions:
    cy, cx = region.centroid
    color = hsv[int(cy), int(cx)][0]
    
    if region.eccentricity == 0:
        circles[color] += 1
    else:
        rects[color] += 1    
    
circles = dict(count(circles))
rects = dict(count(rects))

objects = sum(circles.values()) + sum(rects.values())
print("Objects in dicts: ", objects)

print("Rectangles:")
for key in rects.keys():
    print(f"{key}: {rects[key]}")
print()
print("Circles: ")
for key in circles.keys():
    print(f"{key}: {circles[key]}")
    
plt.imshow(labeled)
plt.show()

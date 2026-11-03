import numpy as np
import matplotlib.pyplot as plt

def create_img():
    x = np.arange(0, 101)
    y = x**2
    image = np.ones((101, 10001, 3), dtype=np.uint8) * 255
   
    for xi, yi in zip(x, y):
        image[xi,yi] = [0, 0, 0]
        if xi + 1 < 101:
            image[xi + 1, yi] = [0, 0, 0]
        if yi + 1 < 10001: 
            image[xi, yi + 1] = [0, 0, 0]
           
    return image  

def draw(image):
    plt.imshow(image, aspect="auto")

img = create_img()
draw(img)
plt.show()
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lena_color_512.tif',1)
plt.imshow(img)
plt.title('Lena')
plt.xticks([])
plt.yticks([])
plt.show()


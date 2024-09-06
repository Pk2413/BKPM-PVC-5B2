import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("/media/prayoga/SSD/coding/latihan python/minggu 2/gambar/IMG_20220902_203508.jpg", cv2.IMREAD_GRAYSCALE)

levels = 4

interval_size = 256 // levels
interval = [ i * interval_size for i in range(levels)]
mid_values = [((i * interval_size) + ((i+1) * interval_size -1 )) // 2 for i in range(levels)]

def quantize(image, interval, mid_values):
    quantized_image =  np.zeros_like(image)
    for i in range(len(interval)):
        lower_bound = interval[i]
        upper_bound = lower_bound + interval_size - 1
        mask = (image >= lower_bound) & (image <= upper_bound)
        quantized_image[mask] = mid_values[i]
    return quantized_image

quantized_image = quantize(image, interval, mid_values)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("gambar asli")
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.axis('off')

plt.show()

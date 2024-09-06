import numpy as np
import cv2
import matplotlib.pyplot as plt

def log_brightness_transform(image):
    # Add a small constant to avoid division by zero
    max_value = np.max(image) + 1e-6
    c = 255 / np.log(1 + max_value)

    # Apply logarithmic brightness transformation
    log_transformed = c * np.log(1 + image + 1e-6)

    # Clip values to the range of 0 to 255 and convert to uint8
    log_transformed = np.clip(log_transformed, 0, 255).astype(np.uint8)

    return log_transformed

# Read the image
image = cv2.imread("D:/coding/latihan python/minggu 2/gambar/IMG_20220902_203508.jpg", cv2.IMREAD_GRAYSCALE)

# Apply logarithmic brightness transformation
log_transformed = log_brightness_transform(image)

# Display the original and transformed images
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Log Brightness Transformed Image")
plt.imshow(log_transformed, cmap="gray", vmin=0, vmax=255)
plt.axis("off")

plt.show()
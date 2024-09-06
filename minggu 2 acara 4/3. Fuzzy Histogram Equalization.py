import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


def membership_fn(x, mean, stddev):
    if stddev == 0:
        stddev = 1e-8
    return np.exp(-((x - mean) ** 2) / (2 * (stddev ** 2)))

# Fuzzy histogram equalization function
def fuzzy_histogram_equalization(image, block_size=16):
    # Convert image to grayscale if required
    if len(image.shape) == 3:  # If the image has 3 channels (RGB)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get image dimensions
    height, width = image.shape

    # Create a blank image to hold the equalized result
    equalized_image = np.zeros_like(image, dtype=np.uint8)

    # Block size for local processing
    block_height = block_size
    block_width = block_size

    # Process each block
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            # Get the current block
            block = image[y:y + block_height, x:x + block_width]

            if block.size == 0:
                continue

            # Calculate local histogram
            hist, bins = np.histogram(block.flatten(), bins=256, range=[0, 256])

            # Compute the CDF (Cumulative Distribution Function)
            cdf = hist.cumsum()
            cdf_normalized = cdf * 255 / (cdf[-1])

            # Apply the CDF to equalize the block
            equalized_block = np.interp(block.flatten(), bins[:-1], cdf_normalized).reshape(block.shape)

            # Calculate fuzzy membership
            mean = np.mean(equalized_block)
            stddev = np.std(equalized_block)
            membership = membership_fn(equalized_block, mean, stddev)

            # Apply fuzzy contrast adjustment
            equalized_image[y:y + block_height, x:x + block_width] = np.clip(equalized_block * membership, 0, 255).astype(np.uint8)

    return equalized_image


current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "gambar", "foto.jpg")

image = cv2.imread(image_path)

fhe_image = fuzzy_histogram_equalization(image)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gambar setelah FHE")
plt.imshow(fhe_image, cmap="gray")
plt.axis("off")

plt.show()

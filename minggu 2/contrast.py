from PIL import Image
import numpy as np

def linear_contrast(input_image_path, output_image_path, contrast_factor):
    img = Image.open(input_image_path)
    img_np = np.array(img, dtype=np.float32)
    img_np = img_np * contrast_factor
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)
    img_out = Image.fromarray(img_np)
    img_out.save(output_image_path)

linear_contrast('C:/Python34/gambar/PA.jpg', 'output_contrast.jpg', 1.2)
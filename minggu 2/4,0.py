from PIL import Image
import numpy as np

gambar = "D:/coding/latihan python/minggu 2/gambar/IMG_20220902_203508.jpg"
output = "D:/coding/latihan python/minggu 2/gambar/output/"

def linear_brightness(input_image_path, output_image_path, brightness_factor):
    img = Image.open(input_image_path)
    img_np = np.array(img, dtype=np.int16)
    img_np = img_np + brightness_factor
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)
    img_out = Image.fromarray(img_np)
    img_out.save(output_image_path)

def linear_contrast(input_image_path, output_image_path, contrast_factor):
    img = Image.open(input_image_path)
    img_np = np.array(img, dtype=np.float32)
    img_np = img_np * contrast_factor
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)
    img_out = Image.fromarray(img_np)
    img_out.save(output_image_path)

def linear_saturation(input_image_path, output_image_path, saturation_factor):
    img = Image.open(input_image_path).convert('RGB')
    img_hsv = img.convert('HSV')
    img_hsv_np = np.array(img_hsv, dtype=np.float32)
    img_hsv_np[..., 1] *= saturation_factor
    img_hsv_np[..., 1] = np.clip(img_hsv_np[..., 1], 0, 255)
    img_hsv = Image.fromarray(img_hsv_np.astype(np.uint8), 'HSV')
    img_out = img_hsv.convert('RGB')
    img_out.save(output_image_path)

def inverse(input_image_path, output_image_path):
    img = Image.open(input_image_path)
    img_np = np.array(img)
    img_np = 255 - img_np
    img_out = Image.fromarray(img_np.astype(np.uint8))
    img_out.save(output_image_path)

inverse(gambar, output +'output_inverse.jpg')
linear_saturation(gambar,output + 'output_saturation.jpg', 1.5)
linear_contrast(gambar,output + 'output_contrast.jpg', 1.2)
linear_brightness(gambar,output + 'brightness_image.jpg', 1)
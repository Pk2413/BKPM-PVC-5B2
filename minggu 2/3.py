from PIL import Image
import numpy as np

image = Image.open("D:/coding/latihan python/minggu 2/gambar/IMG_20220902_203508.jpg")
output = "D:/coding/latihan python/minggu 2/gambar/output/"

image_np = np.array(image)

def rgbToGrayScale(image):
    return np.mean(image, axis=2).astype(np.uint8)

def rgbToGrayScaleLightness(image):
    max_rgb = np.max(image, axis=2)
    min_rgb = np.min(image, axis=2)
    return ((max_rgb + min_rgb) / 2).astype(np.uint8)

def rgbToGrayscaleLuminace(image):
    return(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]).astype(np.uint8)

grayscale_image = rgbToGrayScale(image_np)
grayscale_image_light = rgbToGrayScaleLightness(image_np)
grayscale_image_luminace = rgbToGrayscaleLuminace(image_np)

Image.fromarray(grayscale_image).save(output + '3.grayscale_avarage.jpg')
Image.fromarray(grayscale_image_light).save(output + '3.grayscale_lightness.jpg')
Image.fromarray(grayscale_image_luminace).save(output + '3.grayscale_luminance.jpg')
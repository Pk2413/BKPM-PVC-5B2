from PIL import Image
import numpy as np

def linear_brightness(input_image_path, output_image_path, brightness_factor):
    #membuka gambar
    img = Image.open(r"D:\PERKULIAHAN\SEMESTER 5\5. TIFNJK50705 WORKSHOP PENGELAHAN CITRA DAN VISION\foto\python\gs.jpg")

    #mengubah gambar ke array numpy
    img_np = np.array(img, dtype=np.int16)

    #menambahkan brightness factor ke semua piksel
    img_np = img_np + brightness_factor

    #memastikan nilai piksel tetap dalam rentang [0, 255]
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)

    #mengubah array kembali ke gambar
    img_out = Image.fromarray(img_np)

    #menyimpan gambar asli
    img_out.save(output_image_path)

#contoh penggunaan
linear_brightness('input.jpg', 'output_brightness.jpg', 50)
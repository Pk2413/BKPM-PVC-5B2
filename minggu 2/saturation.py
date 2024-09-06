from PIL import Image
import numpy as np

def linear_saturation(input_image_path, output_image_path, saturation_factor):
    # Membuka gambar dan mengubahnya menjadi RGB
    img = Image.open(input_image_path).convert('RGB')
    
    # Mengubah gambar RGB menjadi HSV
    img_hsv = img.convert('HSV')
    img_hsv_np = np.array(img_hsv, dtype=np.float32)

    # Mengalikan nilai saturasi dengan faktor saturasi
    img_hsv_np[..., 1] *= saturation_factor

    # Membatasi nilai saturasi agar tetap dalam rentang [0, 255]
    img_hsv_np[..., 1] = np.clip(img_hsv_np[..., 1], 0, 255)

    # Mengonversi kembali ke uint8 dan menjadi gambar HSV
    img_hsv = Image.fromarray(img_hsv_np.astype(np.uint8), 'HSV')
    
    # Mengonversi kembali ke RGB
    img_out = img_hsv.convert('RGB')
    
    # Menyimpan gambar keluaran
    img_out.save(output_image_path)

# Panggilan fungsi
linear_saturation("C:\GUI PCV\gambar\inp.jpeg", 'output_saturation.jpg', 1.5)

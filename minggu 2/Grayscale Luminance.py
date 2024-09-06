from PIL import Image
import numpy as np

# Fungsi untuk mengonversi RGB ke Grayscale menggunakan Luminance
def rgb_to_grayscale_luminance(image):
    # Konversi gambar ke array numpy
    img_array = np.array(image)
    
    # Ekstrak channel R, G, B
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    
    # Terapkan rumus luminance
    grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    # Ubah array menjadi gambar kembali
    grayscale_image = Image.fromarray(grayscale.astype('uint8'))
    
    return grayscale_image

# Load gambar RGB
image = Image.open('C:/Users/thinkpad/Documents/semester 5/.vscode/foto/aaa.png')

# Konversi gambar ke Grayscale
grayscale_image = rgb_to_grayscale_luminance(image)

# Simpan hasil konversi
grayscale_image.save('C:/Users/thinkpad/Documents/semester 5/.vscode/foto/abc.png')

# Menampilkan gambar hasil konversi
grayscale_image.show()

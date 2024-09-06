import cv2
from matplotlib import pyplot as plt

# fungsi untuk menampilkan histogram citra
def tampilkan_histogram_citra(image_path):
    # membaca citra dari path direktori
    image = cv2.imread(image_path)

    # konversi citra dari BGR (format default openCV) ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    channels = ('r', 'g', 'b')
    colors = ('red', 'green', 'blue')

    plt.figure(figsize=(10,5))

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])

    plt.title('Histogram untuk setiap kanal warna')
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Jumlah pixel')

    path = r'D:\Belajar Python\foto\Backlog.png'

    tampilkan_histogram_citra(path)
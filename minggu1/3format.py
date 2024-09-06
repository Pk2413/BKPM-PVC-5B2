from PIL import Image

img = Image.open("E:/foto/IMG_20220902_203508.jpg")
img_gray = img.convert("L")
img_gray.save("E:/foto/output/3.img_gray.jpg")

img.save("E:/foto/output/3.compressed_image.jpg", optimaze=True)
from PIL import Image

img = Image.open("E:/foto/IMG_20220902_203508.jpg")
img_resized = img.resize((800,600))
img_resized.save("E:/foto/output/2.rezied_image.jpg")
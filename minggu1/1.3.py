from PIL import Image

image_path = "E:/foto/IMG_20220902_203508.jpg"
img = Image.open(image_path)
img.show()

img_resized = img.resize((100,100))
img_resized.show()
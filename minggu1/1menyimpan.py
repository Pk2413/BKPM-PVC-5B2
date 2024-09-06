from PIL import Image

img = Image.open("E:/foto/IMG_20220902_203508.jpg")

img.save("E:/foto/output/1.image.png")
img.save("E:/foto/output/1.new_image.jpg")
img.save("E:/foto/output/1.image_quality_85.jpg", quality=85)
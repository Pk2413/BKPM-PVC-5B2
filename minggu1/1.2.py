import glob

images = glob.glob("E:/foto/*.jpg")

for image in images:
    print(image)
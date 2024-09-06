import os
from PIL import Image

directory = 'E:/foto'
output_directory = 'E:/foto/output'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(directory, filename)
        img = Image.open(img_path)
        img_resized = img.resize((200, 200))
        img_resized.save(os.path.join(output_directory, filename))
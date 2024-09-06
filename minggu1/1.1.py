import os

directory = "E:/foto/"

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
       print(os.path.join(directory, filename))
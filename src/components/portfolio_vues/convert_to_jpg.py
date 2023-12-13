import os
from PIL import Image
while True:
    path = input("path to the file: ")
    path = path[1:-1]
    img = Image.open(path)
    img.save(f"{path[:-4]}.jpg",optimize=True)
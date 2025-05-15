import os
from PIL import Image

doss = input("name of the photos folder: ")

for file in os.listdir(doss):
    if file == "thumbnails":
        continue
    img = Image.open(f"{doss}/{file}")
    size = img.size
    os.makedirs(f"{doss}/thumbnails", exist_ok=True)
    if size[0] > 1000:
        img.thumbnail((750,1061), Image.Resampling.LANCZOS)
    img.save(f"{doss}/thumbnails/thumb{file}",optimize=True)
    print(f"thumb{file} created")
    
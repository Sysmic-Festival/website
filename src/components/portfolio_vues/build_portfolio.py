# Fichier généré à l'aide de GPT - 4o
# sur la base des anciens morceaux de code

import os
from PIL import Image
import shutil

# === CONFIGURATION ===
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")
MAX_IMAGES = 500
TEMPLATE_FILE = "template.vue"
OUTPUT_DIR = "./"  # Le répertoire de sortie où sera générée la page .vue

# === FONCTIONS ===

def convert_to_jpg(image_path):
    base, ext = os.path.splitext(image_path)
    if ext.lower() != ".jpg":
        try:
            img = Image.open(image_path).convert("RGB")
            new_path = base + ".jpg"
            img.save(new_path, optimize=True)
            print(f"Converti : {image_path} -> {new_path}")
            return new_path
        except Exception as e:
            print(f"Erreur lors de la conversion de {image_path} : {e}")
    return image_path

def create_thumbnails(folder):
    print("\n--- Création des miniatures ---")
    thumb_dir = os.path.join(folder, "thumbnails")
    os.makedirs(thumb_dir, exist_ok=True)
    thumbnails = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isdir(path) or not file.lower().endswith(VALID_EXTENSIONS):
            continue

        # Convert to JPG if needed
        path = convert_to_jpg(path)
        file = os.path.basename(path)

        try:
            img = Image.open(path)
            if img.size[0] > 1000:
                img.thumbnail((750, 1061), Image.Resampling.LANCZOS)

            thumb_name = f"thumb{file}"
            thumb_path = os.path.join(thumb_dir, thumb_name)
            img.save(thumb_path, optimize=True)
            print(f"Miniature créée : {thumb_name}")
            thumbnails.append((file, thumb_name))
        except Exception as e:
            print(f"Erreur avec l'image {file} : {e}")
    return thumbnails

def generate_vue_page(year, thumbnails):
    print("\n--- Génération de la page Vue ---")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"{year}.vue")
    thumb_dir = f"{year}/thumbnails"

    try:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as template, open(output_path, "w", encoding="utf-8") as output:
            lines = template.readlines()
            output.writelines(lines[:8])
            output.write(f'<h1>Année {year}</h1>\n')
            output.write(f'<img class="image_year" src="https://www.sysmic.ch/ressources/portfolio/year_images/{year}.jpg">\n')
            output.writelines(lines[8:13])

            for i, (original, thumb) in enumerate(thumbnails):
                if i >= MAX_IMAGES:
                    break
                output.write('<div class="image">\n')
                output.write(f'<a href="https://www.sysmic.ch/ressources/portfolio/{year}/{original}" class="thumbnail-link">\n')
                output.write(f'<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/{year}/thumbnails/{thumb}" data-src="https://www.sysmic.ch/ressources/portfolio/{year}/{original}">\n')
                output.write('</a>\n</div>\n')

            output.writelines(lines[13:])
        print(f"\nFichier {year}.vue généré dans '{OUTPUT_DIR}'")
    except FileNotFoundError:
        print(f"Fichier template '{TEMPLATE_FILE}' introuvable.")

# === SCRIPT PRINCIPAL ===
if __name__ == "__main__":
    year = input("Année du portfolio : ").strip()
    folder = year

    if not os.path.isdir(folder):
        raise NameError(f"Le dossier '{folder}' n'existe pas. Le terminal est-il bien dans le répertoire << portfolio_vues >> ?")

    thumbnails = create_thumbnails(folder)
    generate_vue_page(year, thumbnails)

    print("\n📁 N'oublie pas d'uploader les fichiers sur :")
    print(f"https://www.sysmic.ch/ressources/portfolio/{year}/")
    print(f"https://www.sysmic.ch/ressources/portfolio/{year}/thumbnails/")

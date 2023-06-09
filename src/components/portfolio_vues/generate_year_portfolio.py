import os

# génère automatiquement une page d'année du portfolio
# Il faut avoir téléchargé en local les images de l'année en question

year=input("année du portfolio: ")
template = open("./src/components/portfolio_vues/template.vue", "r")
filename = "./src/components/portfolio_vues/" + year + ".vue"
dossname = "../portfolio_images/" + year + "/thumbnails"

output = open(filename, "w")
for i in range(8):
    line = template.readline()
    output.write(line)

output.write('<h1>Année {}</h1>\n'.format(year))
output.write('<img class="image_year" src="https://www.sysmic.ch/ressources/portfolio/year_images/{}.jpg">\n'.format(year))

for i in range(5):
    line = template.readline()
    output.write(line)

for filename in os.listdir(dossname):
    filename_data = filename.replace("thumb","")
    output.write('<div class="image">\n')
    output.write('<a href="https://www.sysmic.ch/ressources/portfolio/{}/{}" class="thumbnail-link" target="_blank">\n'.format(year,filename_data))
    output.write('<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/{}/thumbnails/{}" data-src="https://www.sysmic.ch/ressources/portfolio/{}/{}">\n'.format(year, filename,year,filename_data))
    output.write('</a>')
    output.write('</div>\n')

for i in range(215):
    line = template.readline()
    output.write(line)

import os

# génère automatiquement une page d'année du portfolio

# /!\ Faire tourner dans un terminal ouvert sur le répertoire "portfolio_vues"

while True:
    year=input("année du portfolio: ")
    template = open("template.vue", "r")
    filename = year + ".vue"
    dossname = year + "/thumbnails"

    output = open(filename, "w", encoding="utf-8")
    for i in range(8):
        line = template.readline()
        output.write(line)

    output.write('<h1>Année {}</h1>\n'.format(year))
    output.write('<img class="image_year" src="https://www.sysmic.ch/ressources/portfolio/year_images/{}.jpg">\n'.format(year))

    for i in range(5):
        line = template.readline()
        output.write(line)

    i=0
    for filename in os.listdir(dossname):
        if i == 500: break
        filename_data = filename.replace("thumb","")
        output.write('<div class="image">\n')
        output.write('<a href="https://www.sysmic.ch/ressources/portfolio/{}/{}" class="thumbnail-link">\n'.format(year,filename_data))
        output.write('<img class="image_image" src="https://www.sysmic.ch/ressources/portfolio/{}/thumbnails/{}" data-src="https://www.sysmic.ch/ressources/portfolio/{}/{}">\n'.format(year, filename,year,filename_data))
        output.write('</a>')
        output.write('</div>\n')

    for i in range(169):
        line = template.readline()
        output.write(line)
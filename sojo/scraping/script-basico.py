# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
url = "https://ransomwaretracker.abuse.ch/tracker/"
contador = 1
datos = []
peticion = requests.get(url)
statusCode = peticion.status_code
if statusCode != 200:
    exit()
html = BeautifulSoup(peticion.text, "html.parser")
tabla = html.find_all('table', {'class': 'maintable'})
for row in tabla[0].find_all("tr")[1:]:
    dato = zip((td.get_text() for td in row.find_all("td")))
    datos.append(dato)
print "fecha,malware,host"
for dato in datos:
    print str(dato[0][0]) + "," + str(dato[2][0]) + "," + str(dato[3][0]).replace(' ', '')

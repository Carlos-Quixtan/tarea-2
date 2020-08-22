import json
print("-------------------------------------------------------------------------------")
print("ejecutando formato json")
print("-------------------------------------------------------------------------------")

def readJson():
    file = open('formatoJson',)
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = readJson()
for nombre in dict:
    print(nombre)

import xml.etree.ElementTree as ET

print("------------------------------------------------------------------------------")
print("ejecutando formato xml")
print("-------------------------------------------------------------------------------")

tree = ET.parse('carlos')
root = tree.getroot()


for elem in root:
   for subelem in elem:
      print(subelem.text)



import csv

nombre_archivo = 'C:/Users/50232/Desktop/Cuarto Semestre/Lenguages formales/lab/tarea 2/pythonProject/formatocsvv.csv'

with open( nombre_archivo ) as f:
    datos = csv.reader(f)

    lista = list(datos)

    print("--------------------------------------------------------------------------")
    print('ejecutando formato csv')
    print("--------------------------------------------------------------------------")
    print(lista)
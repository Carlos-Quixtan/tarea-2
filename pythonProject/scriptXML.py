import xml.etree.ElementTree as ET

print("-----------------------------------------------------")
print("ejecutando formato xml")
print("-----------------------------------------------------")

tree = ET.parse('carlos')
root = tree.getroot()


for elem in root:
   for subelem in elem:
      print(subelem.text)


#'C://Users/50232/Desktop/Cuarto Semestre/Lenguages formales/lab/tarea 2/formatoXML.xml





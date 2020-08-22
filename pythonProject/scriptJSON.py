import json
print("-----------------------------------------------------")
print("ejecutando formato json")
print("-----------------------------------------------------")

def readJson():
    file = open('formatoJson',)
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = readJson()
for nombre in dict:
    print(nombre)

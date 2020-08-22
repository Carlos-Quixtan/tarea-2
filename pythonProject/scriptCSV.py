import csv

nombre_archivo = 'C://Users/50232/Desktop/Cuarto Semestre/Lenguages formales/lab/tarea 2/formatocsvv.csv'

with open( nombre_archivo ) as f:
    datos = csv.reader(f)

    lista = list(datos)

    print("---------------------------------------------------")
    print('ejecutando formato csv', type(lista))
    print(lista)


import csv
import matplotlib.pyplot as plt


def lee_csv(path):
  with open(path,'r') as file:
    reader = csv.reader(file,delimiter=',') #Lee el archivo CSV con delimitador en comas (,)
    header = next(reader)  #Ubica únicamente la primera fila y la guarda en un arreglo
    paises = []
    for row in reader:
      item = zip(header,row) #Contatena el header con las filas
      dict_paises = {country:i for country,i in item}   #Realiza un cambio a diccionarios
      paises.append(dict_paises) 
    return paises
    
def find_country(country,data):
  for i in data:
    if i['Country/Territory'] == country:
      return i
#Columna 5 hasta la 13
def datos_country(pais):
  valores = list(pais.values())
#  key = list(pais.keys())
  llaves = ['2022','2020','2015','2010','2000','1990','1980','1970']
  population = valores[5:13]
  poblacion = [int(x) for x in population]
  return llaves,poblacion
    
def grafics(labels,values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()
  

def run():
  paises = lee_csv("./app/data.csv")
  pais = input("Ingrese un país: ").capitalize()
  country = find_country(pais,paises)
  if country!=None:
    keys,values = datos_country(country)
    grafics(keys,values)
  else:
    print("País no encontrado en la base de datos")


if __name__ == "__main__":
  run()
  
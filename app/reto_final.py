import reto
import charts

def busca_columna(datos):
  data = []
  paises = []
  data = [percent["World Population Percentage"] for percent in datos]
  paises = [country["Country/Territory"] for country in datos]
  return data,paises
  
#  for j in datos:
#    if j["Country/Territory"]:
#      paises.append(j["Country/Territory"])
  #for i in datos:
  #  if i["World Population Percentage"]:
   #   data.append(i["World Population Percentage"])  

def transforma(percent):
  porcentaje = [round(float(num)*100,3) for num in percent]
  return porcentaje
  

def run():
  datos = reto.lee_csv("./app/data.csv")
  porcent,countries = busca_columna(datos)
  porcentaje_100 = transforma(porcent)
  
  filtro = list(filter(lambda item:item["Continent"]=='South America',datos))
  per,paises = busca_columna(filtro) 
  percent= transforma(per)
  charts.generate_pie_chart(paises,percent)
  #charts.generate_pie_chart(countries,porcentaje_100)

  
  
#  reto.grafics(paises,percent)

if __name__ == "__main__":
  run()
  
    
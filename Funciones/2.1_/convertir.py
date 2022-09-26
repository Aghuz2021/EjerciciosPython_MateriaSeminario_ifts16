#Funciones
def converDias(segundos):
   dias = int((segundos/86400))
   return dias

def converHoras(segundos):
   horas = segundos//3600
   return horas

def converMinutos(segundos):
   minutos = (segundos%3600)//60
   return minutos

def converSegundos(segundos):
   segundos = ((segundos%3600)%60)   
   return segundos

#Ejercion de mi programa
def main():
   segundos = int((input("INGRESE TIEMPO EN SEGUNDOS: ")))
   print(converDias(segundos),"Dia(s),",
         converHoras(segundos),"horas(s),",
         converMinutos(segundos),"minutos(s),",
         converSegundos(segundos),"segundos(s).")

main()
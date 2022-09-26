
def main():
   dia= int(input("ingrese un dia: "))
   mes= int(input("ingrese un mes: "))
   anio= int(input("ingrese un anio: "))
   if boolean_Func(dia, mes,anio) ==  True:
      print(dia,"/",mes,"/",anio," Fecha correcta")
   else: 
      print(dia,"/",mes,"/",anio," Fecha incorrecta")

def boolean_Func(dia:int,mes:int,anio:int):
   FechaValida = True
   FechaInvalida = False 
   
   if mes >=1 and mes <=12 and anio >= 0 and dia >=1 and dia <=31:
      if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia >=1 and dia <=30):
         return FechaValida
      if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or  mes == 8 or mes == 10 or mes == 12) and (dia>=1 and dia <=31):
         return FechaValida
      if ( anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0 ):
         if mes == 2 and (dia >=1 and dia <=29):
            return FechaValida
      if mes == 2 and (dia  >=1 and dia <=28):
         return FechaValida
   return FechaInvalida   

main()
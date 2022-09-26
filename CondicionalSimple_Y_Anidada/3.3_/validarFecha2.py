def main():
   dia= int(input("ingrese un dia: "))
   mes= int(input("ingrese un mes: "))
   anio= int(input("ingrese un anio: "))
   if boolean_Func(dia, mes,anio) ==  True:
      print(dia,"/",mes,"/",anio," Fecha correcta")
   else: 
      print(dia,"/",mes,"/",anio," Fecha incorrecta") 

def anioBiciesto(anio):
   res=False
   if ( anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0 ):
      res = True
      return res
   return res
   
def validarMeses(mes):
   res=False
   for n in range(1,13):
      if mes in range(1,13):
         res = True
         return res
      return res
   
def valdiarDias(dia):
   res=False
   for n in range(1,32):
      if dia in range(1,32) or dia in range(1,31) or dia in range(1,29) or dia in range(1,30):
         res = True
         return res
      return res

def boolean_Func(dia:int,mes:int,anio:int):
   FechaValida = True
   FechaInvalida = False 
   
   
   valdiarAnio= anio >=0
   mesesDeTreintaDias=[4,6,9,11]
   mesesDeTreintaUno=[1,3,5,7,8,10,12]
   mesDos=[2]
   
   if validarMeses(mes) and valdiarAnio and valdiarDias(dia):
      if (mes in mesesDeTreintaDias) and valdiarDias(dia):
         return FechaValida
      if (mes in mesesDeTreintaUno) and valdiarDias(dia):
         return FechaValida
      if (anioBiciesto(anio)):
         if (mes in mesDos) and valdiarDias(dia):
            return FechaValida
      if (mes in mesDos) and valdiarDias(dia):
         return FechaValida
   return FechaInvalida   

main() 
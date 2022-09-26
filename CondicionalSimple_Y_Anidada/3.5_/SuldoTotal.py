def bono(sueldoBase):
   porcentaje =15
   res= porcentaje * sueldoBase/ 100
   if sueldoBase < 2000:
      porcentaje=20
      res= porcentaje * sueldoBase/ 100   
   return res  

def plusH(SueldoBase,tieneHijos):
   porcentaje=5
   if tieneHijos=="s":
      res= porcentaje * SueldoBase/ 100   
      return res
   elif tieneHijos=="n":
      return 0
   
def plusCategoria(sueldoBase,numCategoria):
   categoria1=[4,5,6]
   categoria2=[1,2,3]
   categoria3=[7,8,9]

   if numCategoria in categoria1:
      porcentaje=12
      res=porcentaje * sueldoBase/100
      return res
   
   elif numCategoria in categoria2:
      porcentaje=10
      res=porcentaje * sueldoBase/100
      return res
      
   elif numCategoria in categoria3:
      porcentaje=20
      res=porcentaje * sueldoBase/100
      return res
   
def plus(sueldoBase,Hijo,categoria):
   plusHijos= plusH(sueldoBase, Hijo) 
   plusCategorias=plusCategoria(sueldoBase,categoria)
   bonos=bono(sueldoBase)
   if plusHijos:
      if plusCategorias:
         if categoria in range(7,10):
            return plusCategorias + sueldoBase + bonos
   return plusCategorias + sueldoBase + bonos+ plusHijos

def main():
   sueldoBase=int(input("*Ingrese su sueldo Base: "))

   Hijo=input("*Tiene hijos marque con s/n: ")
   categoria=int(input("*Ingrese una categoria 1 al 9: "))
   print("Calculo total es:","$",plus(sueldoBase, Hijo, categoria))
   
main() 
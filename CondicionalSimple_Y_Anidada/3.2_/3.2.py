def numReal_Func(NumReal):
   negativo="El numero es negativo"
   positivo="El numero es positivo"
   cero="El numero es cero"
   
   if NumReal == 0:
      return cero
   elif NumReal < 0:
      return negativo
   else:
      return positivo

def numRecibido_Func(numRecibido):
#castea numeroRecibido a int y lo guarda en numeneroNatural 
   numEnteroNatural = int(numRecibido)
   if numRecibido == numEnteroNatural:
      if numRecibido > int(0):
         return "y entero natural"
# numRecibido ingresa como float
   if numRecibido == 0:
         return "y entero"
   if numRecibido < 0:
         return "y entero"
   if numRecibido > 0:
      return "y real."
   
def main():
   num= input("Escribe un número: ")
   numero = float(num)
   print(numReal_Func(numero),numRecibido_Func(numero))
   
main()
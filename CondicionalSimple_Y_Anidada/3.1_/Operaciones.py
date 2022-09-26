def operar_func(num1,num2,src):
   
   if src == "+":
      suma=num1 + num2
      return suma
   if src == "-":
      resta=num1 - num2
      return resta
   if src == "*":
      multiplicacion=num1 * num2
      return multiplicacion
   if src == "/":
      division=num1 / num2
      return division
   if src == "//":
      divisionEntero = num1 // num2
      return divisionEntero
   if  src == "**":
      potencias=num1 ** num2
      return  potencias


def main():
   num1 = int(input("Ingrese el primer numero:"))
   num2 = int(input("Ingrese el segundo numero:"))
   src = input("Ingese la operacion(+,-,*,/,//,**)")
   
   result = operar_func(num1, num2, src)
   print(num1,src,num2,"=",result)
   
main()
Una empresa necesita calcular el suldo total que dara a sus empleados
a fin de este año. Parra ello se sigue el siguiente criterio:

Si el suldo supera los $2000, el bono sera del 15%. de lo contrario, el bono sera de 20%

Ademas recibira un plus de acuerdo al siguiente criterio:
   Si el empleado tiene Hijos se suma un plus del 5% del sueldo.
   Si el empleado pertenece a la categoria 1-2-3 recibe 10% del suldo.
   si pertenece a la categoria 4-5-6 recibe un 12% del sueldo. Si es de la categoria 7-8-9 recibe un 20% delmsueldo pero no cobra el plus por tener hijos.

Realizar un programa que solicite al usuario la info necesaria(suldo base,hijos(s/n) y categoria) para luego calcular el sueldo total. Para el calculo del sueldo total se debera resolver invocando a las siguientes funciones:

La primer funcion: Bono recibe por parametro el sueldo base, luego calcula y retorna el valor del bono.

La segnda funcion:Plus recibe por parametro el sueldo base, si tiene hijos o no y la categoria. Esta funcion debe retornar la suma del plus por hijo y resolver el plus por categoria debera invocar a plusC.

La tercera duncion: plusH recibe dos parametros el sueldo base y otra variable que indica si tiene hijo. Luego calcular y retornar el plus por hijo.

La cuarta funcion: plusC recibe como prametro el suldo base y el numero de categoria, luego calcula y retorna el plus categoria

Desde el programa main solicitar al usuari el ingreso de los datos, luego invocar a las funciones que correspondan y por ultimo msotrar por pantalla el total a pagar al empleado
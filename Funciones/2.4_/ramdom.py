import  random
def aleatorio_Func(limiteInferior,limiteSuperior):
    resulNumAletorio = random.randint(limiteInferior,limiteSuperior)
    return resulNumAletorio

def main():
    limite_Inferior = int(input("Ingresar límite inferior: "))
    limite_Superior = int(input("Ingresar límite superior: "))

    resul1= (aleatorio_Func(limite_Inferior,limite_Superior,))
    resul2= (aleatorio_Func(resul1,limite_Superior,))
    resul3= (aleatorio_Func(resul1,resul2))

    print("1-limite inferior {}, limite superior {}. Numero generado:{}".format(limite_Inferior,limite_Superior,resul1))
    print("2-limite inferior {}, limite superior {}. Numero generado:{}".format(resul1,limite_Superior,resul2))
    print("3-limite inferior {}, limite superior {}. Numero generado:{}".format(resul1,resul2,resul3))


main()
print("Bienvenido, este programa le solicita que un numero de pesos, una tasa de interes y cantidad de años y le devuvelve su beneficio.")
pesos = float(input("Ingrese el monto en pesos: "))
tasa = float(input("Ingrese la tasa de interes: "))
años = float(input("Ingrese la cantidad de años: "))
beneficio = pesos * ((1 + tasa%100) ** años)
print("El beneficio obtenido es de", beneficio ,"pesos")
listaEst = []
resp = "Si"
while(resp.upper() !="NO"): #Convertir en mayus las minisculas
    tam = len(listaEst) #len tamaño de un arreglo
    print("Elementos guardados: ", tam)
    nombres = input("Escriba el nombre del estudiante: ")
    listaEst.append(nombres)
    resp = input("Desea agregar mas? SI - NO: ")
for est in listaEst:
    print(est)
#Sumar los elementos de un arreglo
arreglo = []
cant=int(input("Dime cuantos #: "))
cont = 0
while(cont <cant):
    num = int(input("Dime un #: "))
    arreglo.append(num)
    cont+=1
suma = 0
for num in arreglo:
    suma +=num
print("La suma es", suma)
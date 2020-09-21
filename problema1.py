print()
lista=[]
for i in range(20):
    lista.append(int(input("Introduzca un numero: ")))
    
print("\n Lista impresa: ")
print(lista)
print("\n Lista ordenada: ")
ordenada=sorted(lista)
print(ordenada)
print("\nLongitud: ")
print(len(lista))
print("\n--------------------------------------------------------------")

n=1
while n==1:
    x=int(input("Introduzca un numero para buscarlo dentro de la lista: "))
    if x in lista:
        print("Encontrado")
    else:
        print("Este numero no se encuentra en su lista...")

    n=int(input("\nSi desea buscar otro numero en esta lista introduzca el numero (1): "))
    
    
print("\nPrograma finalizado...\n")
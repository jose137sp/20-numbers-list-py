
print()
lista=[]
x=(int(input("Introduca con un número la cantidad de palabras que desea insertar en la lista del programa: ")))
print()
for i in range(x):
    lista.append(input("Introduzca una palabra: "))

lista_invertida=[]
for elem in lista:
    lista_invertida.append(elem[::-1])

def inversas(lista):  
    lista_inv_2=[]
    for word in lista:
        if word in lista_invertida:
            lista_inv_2.append(word)
    return lista_inv_2

print("\nLas palabras inversas ingresadas son: ")
print(inversas(lista))
print("\n Programa Finalizado...\n")

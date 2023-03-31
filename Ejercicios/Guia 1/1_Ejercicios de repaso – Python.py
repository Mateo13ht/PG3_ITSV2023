#Ejercicio 1
print("Ejercicio 1")
def eje1(lista, elemento):
    try:
        index = lista.index(elemento)
        return index
    except ValueError:
        return None

lista = [2, 3, 8, 45, 59, 80, 2005]
elemento = int(input("Ingresa el número a buscar: "))
index = eje1(lista, elemento)

if index is not None:
    print(f"El número {elemento} se encuentra en el índice {index} de la lista.")
else:
    print(f"El número {elemento} no se encuentra en la lista.")


#Ejercicio 2
print("\nEjercicio 2")
def eje2(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

anio = int(input("Ingrese un año: "))
if eje2(anio):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")   
    

#Ejercicio 3    
print("\nEjercicio 3")
ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))
caracter = input("Ingrese el caracter para dibujar el rectángulo: ")

for i in range(alto):
    for j in range(ancho):
        print(caracter, end=" ")
    print()   

#Ejercicio 4
print("\nEjercicio 4")
def eje4(lista):
    return sorted(lista, reverse=True)

lista_numeros = [3, 7, 1, 9, 2, 8, 4, 6, 50, 620]
lista_ordenada = eje4(lista_numeros)
print(lista_ordenada) 

#Ejercicio 5
print("\nEjercicio 5")
def eje5(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

print(eje5("neuquen")) 
print(eje5("jovenes")) 
print(eje5("anana")) 
print(eje5("papa")) 
print(eje5("pelado")) 


#Ejercicio 6
print("\nEjercicio 6")
def eje6(frase):
    vocales = ["a", "e", "i", "o", "u"]
    frase = frase.lower()
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador

frase = "La vida es un camino de aprendizaje constante, en el que cada paso nos lleva a descubrir algo nuevo sobre nosotros mismos y el mundo que nos rodea"
print(eje6(frase)) 

#Ejercicio 7
print("\nEjercicio 7")
def eje7(numero):
    cadena = str(numero)
    for i in range(len(cadena) - 1):
        diferencia = abs(int(cadena[i+1]) - int(cadena[i]))
        if diferencia != 1:
            return False
    return True
print(eje7(123234))
print(eje7(9876787654))
print(eje7(1256))
print(eje7(1251256))
print(eje7(128416))
print(eje7(1245236))

#Desafio
print("Desafio")
ancho = int(input("Introduce el ancho del triángulo: "))
alto = int(input("Introduce el alto del triángulo: "))
caracter = input("Introduce el carácter a utilizar en el dibujo: ")

for i in range(alto):
    for j in range(ancho - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print(caracter, end="")
    print()
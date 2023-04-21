#Ejerciocio 1
print("\nEjercicio 1")
while True:
    try:
        num1=int(input("Ingrse el primer numero:"))
        num2=int(input("Ingrse el segundo numero:"))
        suma= num1+num2
        print("El resultado de la suma es:",suma)
        opcion = input("¿Desea seguir sumando valores? (S/N): ")
        if opcion.upper() != "S":
            break
    except ValueError:
        print("Ingrese un valor valido")
    
#Ejerciocio 2 y 4
print("\nEjercicio 2 y 4")
while True:
    try:
        num1=int(input("Ingrse el primer numero:"))
        num2=int(input("Ingrse el segundo numero:"))
        div= num1/num2
        print("la divicion entre",num1,"y",num2,"es:",div)
        opcion = input("¿Desea seguir sumando valores? (S/N): ")
        if opcion.upper() != "S":
            break
    except ZeroDivisionError:
        print("Nos se puede dividir por cero")
    except ValueError:
        print("Ingrese un valor valido")      
#Ejerciocio 4  
print("\nEjercicio 4")

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    numero_mes = int(input("Ingresa el número de mes (1-12): "))
    mes = meses[numero_mes - 1]
    print("El mes correspondiente es:", mes)
except IndexError:
    print("Número de mes inválido. Por favor ingresa un número entre 1 y 12.")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero entre 1 y 12.")

#Ejercicio 5
print("\nEjercicio 5")
strings = ["Hola", "que", "tal", "como", "estas", 10]
with open("Ejercicios/Guia 3/act5.txt", "w") as f:
    for string in strings:
        try:
            f.write(str(string) + "\n")
        except TypeError as e:
            print(f"Error: {e}. No se pudo escribir el elemento {string} en el archivo.")
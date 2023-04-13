#Ejerciocio 1
print("\nEjerciocio 1")
class Persona:
    def __init__(self):
        self.nombre = ""
        
    def inicializar_nombre(self):
        self.nombre = input("Ingrese el nombre: ")
        
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)
persona1 = Persona()
persona1.inicializar_nombre()
persona1.mostrar_nombre() 

persona2 = Persona()
persona2.inicializar_nombre()
persona2.mostrar_nombre() 


#Ejerciocio 2
print("\nEjerciocio 2")
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
        
    def esta_regular(self):
        if self.nota >= 6:
            print("El alumno", self.nombre, "está regular")
        else:
            print("El alumno", self.nombre, "no está regular")

nombre1 = input("Ingrese el nombre del primer alumno: ")
nota1 = float(input("Ingrese la nota del primer alumno: "))
alumno1 = Alumno(nombre1, nota1)

nombre2 = input("Ingrese el nombre del segundo alumno: ")
nota2 = float(input("Ingrese la nota del segundo alumno: "))
alumno2 = Alumno(nombre2, nota2)

alumno1.imprimir_datos()
alumno1.esta_regular() 

alumno2.imprimir_datos()
alumno2.esta_regular()


#Ejerciocio 3
print("\nEjerciocio 3")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", mayor)
        
    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")
lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))
lado3 = int(input("Ingrese el valor del lado 3: "))

triangulo = Triangulo(lado1, lado2, lado3)

triangulo.imprimir_lado_mayor() 
triangulo.es_equilatero() 

#Ejerciocio 4
print("\nEjerciocio 4")

class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número: "))
        self.num2 = int(input("Ingrese el segundo número: "))
        self.mostrar_resultados()
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def mostrar_resultados(self):
        print("Suma:", self.suma())
        print("Resta:", self.resta())
        print("Multiplicación:", self.multiplicacion())
        print("División:", self.division())
operaciones = Operaciones()

#Ejerciocio 5
print("\nEjerciocio 5")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))
    
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre="", edad=0, sueldo=0):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Sueldo:", self.sueldo)
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

persona1 = Persona("", 0)
persona1.cargar_datos()
print("Datos de la persona:")
persona1.mostrar_datos()

empleado1 = Empleado("", 0, 0)
empleado1.cargar_datos()
print("Datos del empleado:")
empleado1.mostrar_datos()

#Ejerciocio 6
print("\nEjerciocio 6")
class Familia:
    def __init__(self, nombre_padre, nombre_madre, hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos
    
    def __str__(self):
        nombres_hijos = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}, Madre: {self.nombre_madre}, Hijos: {nombres_hijos}"

nombre_padre = input("Ingrese el nombre del padre: ")
nombre_madre = input("Ingrese el nombre de la madre: ")
num_hijos = int(input("Ingrese la cantidad de hijos: "))

hijos = []
for i in range(num_hijos):
    nombre_hijo = input(f"Ingrese el nombre del hijo {i+1}: ")
    hijos.append(nombre_hijo)

familia = Familia(nombre_padre, nombre_madre, hijos)
print(familia)

# Reto-test Python

# Ejercicio 1
def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("Hola mundo"))


# Ejercicio 2
def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print(calcular_promedio([4, 8, 6, 2]))


# Ejercicio 3
def encontrar_duplicado(lista):
    vistos = []
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)
    return None

print(encontrar_duplicado([3, 5, 1, 5, 3]))


# Ejercicio 4
def enmascarado_datos(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarado_datos(1234567890123456))


# Ejercicio 5
def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1 == palabra2:
        return False
    return sorted(palabra1) == sorted(palabra2)

print(es_anagrama("Roma", "amor"))
print(es_anagrama("hola", "adios"))


# Ejercicio 6
def buscar_nombre():
    nombres = input("Escribe los nombres separados por comas: ").split(",")
    nombres = [n.strip() for n in nombres]
    nombre = input("Que nombre quieres buscar? ").strip()
    if nombre in nombres:
        print("El nombre", nombre, "esta en la lista")
    else:
        raise Exception("El nombre " + nombre + " no esta en la lista")

# Probar con: Jaime, Silvia, Ana
try:
    buscar_nombre()
except Exception as e:
    print("Error:", e)


# Ejercicio 7
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(5):
    print(fibonacci(i))


# Ejercicio 8
def encontrar_puesto_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] + " " + empleado["apellido"] == nombre_completo:
            return empleado["puesto"]
    return nombre_completo + " no trabaja aqui"

empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
             {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
             {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

print(encontrar_puesto_empleado("Isabel Martín", empleados))
print(encontrar_puesto_empleado("Pedro López", empleados))


# Ejercicio 9
cubo_numero = lambda x: x ** 3
print(cubo_numero(3))


# Ejercicio 10
resto_division = lambda a, b: a % b
print(resto_division(17, 5))


# Ejercicio 11
lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(numeros_pares)


# Ejercicio 12
numeros_suma = list(map(lambda x: x + 3, lista_numeros))
print(numeros_suma)


# Ejercicio 13
lista_numeros_1 = [1, 4, 5, 6, 7, 7]
lista_numeros_2 = [3, 11, 34, 56]
sumar_listas = list(map(lambda a, b: a + b, lista_numeros_1, lista_numeros_2))
print(sumar_listas)


# Ejercicio 14
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {"tronco": self.tronco,
                "num_ramas": len(self.ramas),
                "ramas": self.ramas}

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())


# Ejercicio 15
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise Exception(self.nombre + " no tiene saldo suficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario.cuenta_corriente or not self.cuenta_corriente:
            raise Exception("Los dos usuarios necesitan cuenta corriente")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

alicia.agregar_dinero(20)
print("Saldo Alicia:", alicia.saldo)

try:
    alicia.transferir_dinero(bob, 80)
except Exception as e:
    print("Error:", e)

alicia.retirar_dinero(50)
print("Saldo Alicia:", alicia.saldo)
print("Saldo Bob:", bob.saldo)


# Ejercicio 16
def contar_palabras(texto):
    contador = {}
    for palabra in texto.split():
        palabra = palabra.strip(".,").lower()
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    return texto.replace(palabra + " ", "")

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opcion no valida"

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))

# Ejercicios Introducción a Python

# Ejercicio 1: Conversor de Temperatura
celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(celsius, "ºC son", fahrenheit, "ºF")


# Ejercicio 2: Calculadora de Propina
cuenta = float(input("Total de la cuenta: "))
propina = cuenta * 0.15
total = cuenta + propina
print("Propina:", round(propina, 2))
print("Total a pagar:", round(total, 2))


# Ejercicio 3: Verificación de Edad
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Ejercicio 4: Contador de Vocales
palabra = input("Escribe una palabra: ").lower()
vocales = 0
for letra in palabra:
    if letra in "aeiouáéíóú":
        vocales += 1
print("La palabra tiene", vocales, "vocales")


# Ejercicio 5: Suma de Números Pares
suma = 0
for numero in range(2, 101, 2):
    suma += numero
print("La suma de los pares del 1 al 100 es", suma)


# Ejercicio 6: Verificación de Palíndromo
palabra = input("Escribe una palabra: ").lower()
if palabra == palabra[::-1]:
    print(palabra, "es un palíndromo")
else:
    print(palabra, "no es un palíndromo")


# Ejercicio 7: Calculadora Simple
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("Resultado:", num1 / num2)
else:
    print("Operación no válida")


# Ejercicio 8: Cálculo del IMC
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros (ej: 1.70): "))
imc = peso / altura ** 2
print("Tu IMC es", round(imc, 2))


# Ejercicio 9: Conversor de Divisas
dolares = float(input("Cantidad en dólares: "))
euros = dolares * 0.85
print(dolares, "dólares son", round(euros, 2), "euros")


# Ejercicio 10: Día de la Semana
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
numero = int(input("Número del 1 al 7: "))
if 1 <= numero <= 7:
    print("El día es", dias[numero - 1])
else:
    print("Número no válido")


# Ejercicio 11: Calculadora de Edad
from datetime import date

anio_nacimiento = int(input("¿En qué año naciste? "))
anio_actual = date.today().year
edad = anio_actual - anio_nacimiento
print("Tienes (o cumplirás este año)", edad, "años")


# Ejercicio 12: Área de un Rectángulo
longitud = float(input("Longitud: "))
ancho = float(input("Ancho: "))
area = longitud * ancho
print("El área del rectángulo es", area)


# Ejercicio 13: Número Primo
numero = int(input("Escribe un número: "))
es_primo = True
if numero < 2:
    es_primo = False
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")


# Ejercicio 14: Calculadora de Descuento
precio = float(input("Precio del artículo: "))
descuento = precio * 0.20
precio_final = precio - descuento
print("Precio final con el 20% de descuento:", round(precio_final, 2))


# Ejercicio 15: Conversor de Tiempo
minutos_totales = int(input("Número de minutos: "))
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(minutos_totales, "minutos son", horas, "horas y", minutos, "minutos")


# Ejercicio 16: Contador de Pares e Impares
numeros = input("Escribe números separados por espacios: ").split()
pares = 0
impares = 0
for n in numeros:
    if int(n) % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Impares:", impares)


# Ejercicio 17: Millas a Kilómetros
millas = float(input("Distancia en millas: "))
km = millas * 1.60934
print(millas, "millas son", round(km, 2), "km")


# Ejercicio 18: Contador de Palabras
frase = input("Escribe una frase: ")
palabras = frase.split()
print("La frase tiene", len(palabras), "palabras")


# Ejercicio 19: Año Bisiesto
anio = int(input("Escribe un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(anio, "es bisiesto")
else:
    print(anio, "no es bisiesto")


# Ejercicio 20: Suma de Números en una Lista
numeros = input("Escribe números separados por espacios: ").split()
suma = 0
for n in numeros:
    suma += float(n)
print("La suma es", suma)
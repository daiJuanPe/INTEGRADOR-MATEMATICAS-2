from itertools import product  # Importa función para producto cartesiano de iterables
from datetime import datetime  # Importa módulo para manejo de fechas y horas

def obtener_digitos_unicos(dni):
    # Convierte el DNI en string, extrae cada dígito, lo convierte a int y crea un conjunto con dígitos únicos
    return set(int(d) for d in str(dni))

def calcular_operaciones_conjuntos(conjuntos):
    # Desempaqueta los tres conjuntos A, B y C
    A, B, C = conjuntos
    # Retorna un diccionario con varias operaciones entre los conjuntos
    return {
        "Unión (A ∪ B ∪ C)": A | B | C,  # Unión de los tres conjuntos
        "Intersección (A ∩ B ∩ C)": A & B & C,  # Elementos comunes a los tres conjuntos
        "Diferencia (A - B)": A - B,  # Elementos en A que no están en B
        "Diferencia (B - C)": B - C,  # Elementos en B que no están en C
        "Diferencia (C - A)": C - A,  # Elementos en C que no están en A
        "Diferencia Simétrica (A Δ B)": A ^ B,  # Elementos en A o B pero no en ambos
        "Diferencia Simétrica (A Δ C)": A ^ C,  # Elementos en A o C pero no en ambos
        "Diferencia Simétrica (B Δ C)": B ^ C,  # Elementos en B o C pero no en ambos
    }

def contar_frecuencias(dni):
    # Inicializa diccionario con claves '0' a '9' y valores 0
    frecuencias = {str(i): 0 for i in range(10)}
    # Cuenta la cantidad de veces que aparece cada dígito en el DNI
    for d in str(dni):
        frecuencias[d] += 1
    return frecuencias  # Retorna el diccionario con frecuencias

def suma_digitos(dni):
    # Suma los dígitos individuales del DNI convertidos a enteros
    return sum(int(d) for d in str(dni))

def evaluar_expresiones_logicas(conjuntos):
    mensajes = []  # Lista para guardar mensajes que cumplan condiciones
    # Si todos los conjuntos tienen al menos 5 elementos, agrega un mensaje
    if all(len(c) >= 5 for c in conjuntos):
        mensajes.append("✔ Todos los conjuntos tienen al menos 5 elementos → Diversidad numérica alta")
    # Encuentra los dígitos comunes a todos los conjuntos
    digitos_comunes = set.intersection(*conjuntos)
    # Si hay dígitos comunes, agrega mensaje con esos dígitos ordenados
    if digitos_comunes:
        mensajes.append(f"✔ Dígito(s) compartido(s) en todos: {sorted(digitos_comunes)}")
    return mensajes  # Retorna lista de mensajes

def es_bisiesto(anio):
    # Determina si un año es bisiesto según las reglas del calendario gregoriano
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def operaciones_anios(anios):
    anio_actual = datetime.now().year  # Obtiene el año actual
    # Calcula edades restando año de nacimiento al actual
    edades = [anio_actual - a for a in anios]
    # Cuenta cuántos años de nacimiento son pares
    pares = sum(1 for a in anios if a % 2 == 0)
    # Cantidad de años impares, calculado como total menos pares
    impares = len(anios) - pares
    mensajes = [
        f"✔ Cantidad de nacidos en año par: {pares}",
        f"✔ Cantidad de nacidos en año impar: {impares}"
    ]
    # Si todos nacieron después del año 2000, agrega mensaje
    if all(a > 2000 for a in anios):
        mensajes.append("✔ Todos nacieron después del 2000 → Grupo Z")
    # Si al menos uno nació en año bisiesto, agrega mensaje
    if any(es_bisiesto(a) for a in anios):
        mensajes.append("✔ Al menos uno nació en un año bisiesto → Año especial")
    # Calcula producto cartesiano de años y edades (tuplas (año, edad))
    producto_cartesiano = list(product(anios, edades))
    return mensajes, producto_cartesiano  # Retorna mensajes y lista de tuplas

# ---------------------------
# Programa principal
# ---------------------------
print("\n╔═══════════════════════════════════════════════════╗")
print("║   Trabajo Integrador 2: Matemática y Programación ║")
print("╚═══════════════════════════════════════════════════╝\n")

# Inicializa lista para guardar DNIs ingresados
dnis = []
print("Ingrese 3 DNIs (presione Enter para usar valores de prueba):")
# Ciclo para pedir 3 DNIs al usuario
for i in range(3):
    entrada = input(f"- DNI del integrante {i+1}: ").strip()  # Lee entrada y elimina espacios
    # Si se presiona Enter sin ingresar nada, usa DNIs de prueba
    if entrada == "":
        dnis = [36876159, 33569007, 32238178]
        print("Se usaron los DNIs de prueba:", dnis)
        break  # Sale del ciclo
    # Si la entrada es numérica, la convierte a entero y agrega a lista
    elif entrada.isdigit():
        dnis.append(int(entrada))
    else:
        print("DNI inválido. Intente de nuevo.")  # Mensaje para entrada inválida
        exit()  # Termina programa si hay error

# Genera conjuntos de dígitos únicos para cada DNI
conjuntos = [obtener_digitos_unicos(dni) for dni in dnis]
print("\n╔══════════════════════╗")
print("║ Conjuntos generados  ║")
print("╚══════════════════════╝")
# Muestra cada conjunto con letra A, B, C y sus dígitos ordenados
for i, conj in enumerate(conjuntos):
    print(f"Conjunto {chr(65+i)} (DNI {dnis[i]}): {sorted(conj)}")

# Realiza y muestra operaciones entre conjuntos
print("\n╔═════════════════════════════════╗")
print("║ Operaciones entre los conjuntos ║")
print("╚═════════════════════════════════╝")
operaciones = calcular_operaciones_conjuntos(conjuntos)
for nombre, resultado in operaciones.items():
    print(f"{nombre}: {sorted(resultado)}")  # Muestra resultado ordenado

# Muestra frecuencias de dígitos y suma para cada DNI
print("\n╔════════════════════════════════╗")
print("║ Frecuencias y suma de dígitos  ║")
print("╚════════════════════════════════╝")
for i, dni in enumerate(dnis):
    frec = contar_frecuencias(dni)  # Cuenta frecuencia de dígitos
    suma = suma_digitos(dni)  # Suma dígitos
    print(f"DNI {dni} → Frecuencias: {frec} | Suma: {suma}")

# Evalúa condiciones lógicas sobre los conjuntos y muestra mensajes
print("\n╔═══════════════════════════════════╗")
print("║ Evaluación de condiciones lógicas ║")
print("╚═══════════════════════════════════╝")
for mensaje in evaluar_expresiones_logicas(conjuntos):
    print("-", mensaje)

# Define años de nacimiento de prueba
anios = [1986, 1998, 2004]
print("\n╔════════════════════════════════╗")
print("║ Años de nacimiento (de prueba) ║")
print("╚════════════════════════════════╝")
print("Años:", anios)
# Ejecuta operaciones sobre años y obtiene mensajes y producto cartesiano
mensajes_anios, producto = operaciones_anios(anios)
for mensaje in mensajes_anios:
    print("-", mensaje)

# Muestra producto cartesiano (tuplas año, edad)
print("\n╔═════════════════════════════════╗")
print("║ Producto cartesiano (año, edad) ║")
print("╚═════════════════════════════════╝")
for par in producto:
    print(par)

print("\n✅ Fin del programa.\n")

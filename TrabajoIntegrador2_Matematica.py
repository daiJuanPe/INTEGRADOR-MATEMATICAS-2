from itertools import product  # Importa 'product' para calcular el producto cartesiano entre listas
from datetime import datetime  # Importa 'datetime' para obtener el año actual

# Función que obtiene los dígitos únicos del DNI y los convierte en un conjunto
def obtener_digitos_unicos(dni):
    return set(int(d) for d in str(dni))  # Convierte el DNI a string, separa cada dígito y lo almacena como entero en un set (elimina duplicados)

# Función que realiza operaciones entre dos conjuntos
def calcular_operaciones_conjuntos(A, B):
    return {
        "Unión (A ∪ B)": A | B,                 # Unión: todos los elementos que están en A o B
        "Intersección (A ∩ B)": A & B,          # Intersección: elementos comunes a A y B
        "Diferencia (A - B)": A - B,            # Diferencia: elementos que están en A pero no en B
        "Diferencia (B - A)": B - A,            # Diferencia: elementos que están en B pero no en A
        "Diferencia Simétrica (A Δ B)": A ^ B,  # Diferencia simétrica: elementos que están en A o en B pero no en ambos
    }

# Función que cuenta cuántas veces aparece cada dígito en un DNI
def contar_frecuencias(dni):
    frecuencias = {str(i): 0 for i in range(10)}  # Inicializa un diccionario con los dígitos 0–9 en 0
    for d in str(dni):                            # Recorre cada dígito del DNI (convertido en string)
        frecuencias[d] += 1                       # Incrementa la frecuencia del dígito correspondiente
    return frecuencias

# Función que suma todos los dígitos del DNI
def suma_digitos(dni):
    return sum(int(d) for d in str(dni))  # Convierte los dígitos del DNI a enteros y los suma

# Función que evalúa condiciones lógicas entre dos conjuntos A y B
def evaluar_expresiones_logicas(A, B):
    mensajes = []

    # Verifica si A tiene más elementos que B y contiene al menos un número impar
    impares_A = {x for x in A if x % 2 != 0}  # Filtra los números impares del conjunto A
    if len(A) > len(B) and impares_A:
        mensajes.append("✔ El conjunto A tiene más elementos que B y contiene números impares → Se considera un conjunto mayor e impar")

    # Verifica si hay dígitos comunes entre A y B
    comunes = A & B
    if comunes:
        mensajes.append(f"✔ Dígito(s) compartido(s) en ambos conjuntos: {sorted(comunes)}")

    return mensajes  # Devuelve los mensajes generados por las condiciones lógicas evaluadas

# Función que determina si un año es bisiesto
def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)  # Regla de años bisiestos

# Función que analiza una lista de años de nacimiento
def operaciones_anios(anios):
    anio_actual = datetime.now().year              # Obtiene el año actual
    edades = [anio_actual - a for a in anios]      # Calcula la edad de cada persona
    pares = sum(1 for a in anios if a % 2 == 0)     # Cuenta cuántos nacieron en año par
    impares = len(anios) - pares                   # El resto son nacidos en años impares
    mensajes = [
        f"✔ Cantidad de nacidos en año par: {pares}",
        f"✔ Cantidad de nacidos en año impar: {impares}"
    ]
    if all(a > 2000 for a in anios):               # Verifica si todos nacieron después del año 2000
        mensajes.append("✔ Todos nacieron después del 2000 → Grupo Z")
    if any(es_bisiesto(a) for a in anios):         # Verifica si alguno nació en un año bisiesto
        mensajes.append("✔ Al menos uno nació en un año bisiesto → Año especial")
    
    producto_cartesiano = list(product(anios, edades))  # Calcula el producto cartesiano entre los años y las edades
    return mensajes, producto_cartesiano

# ---------------------------
# Programa principal
# ---------------------------
print("\n╔═══════════════════════════════════════════════════╗")
print("║   Trabajo Integrador 2: Matemática y Programación ║")
print("╚═══════════════════════════════════════════════════╝\n")

dnis = []  # Lista para almacenar los dos DNIs

print("Ingrese 2 DNIs (presione Enter para usar valores de prueba):")
for i in range(2):  # Solicita los DNIs de los 2 integrantes
    entrada = input(f"- DNI del integrante {i+1}: ").strip()
    if entrada == "":  # Si se presiona Enter sin ingresar nada
        dnis = [36876159, 32238178]  # Usa DNIs de prueba
        print("Se usaron los DNIs de prueba:", dnis)
        break
    elif entrada.isdigit():         # Verifica que la entrada sea numérica
        dnis.append(int(entrada))   # Agrega el DNI a la lista
    else:
        print("DNI inválido. Intente de nuevo.")  # Mensaje de error por entrada inválida
        exit()                                     # Termina el programa

# Genera los conjuntos A y B a partir de los DNIs
A, B = [obtener_digitos_unicos(dni) for dni in dnis]  # Aplica la función a cada DNI
print("\n╔══════════════════════╗")
print("║ Conjuntos generados  ║")
print("╚══════════════════════╝")
print(f"Conjunto A (DNI {dnis[0]}): {sorted(A)}")  # Muestra los dígitos únicos del primer DNI
print(f"Conjunto B (DNI {dnis[1]}): {sorted(B)}")  # Muestra los dígitos únicos del segundo DNI

# Realiza operaciones entre conjuntos A y B
print("\n╔═════════════════════════════════╗")
print("║ Operaciones entre los conjuntos ║")
print("╚═════════════════════════════════╝")
operaciones = calcular_operaciones_conjuntos(A, B)  # Calcula las operaciones de conjuntos
for nombre, resultado in operaciones.items():
    print(f"{nombre}: {sorted(resultado)}")  # Muestra los resultados ordenados

# Muestra las frecuencias de dígitos y la suma de los mismos por cada DNI
print("\n╔════════════════════════════════╗")
print("║ Frecuencias y suma de dígitos  ║")
print("╚════════════════════════════════╝")
for i, dni in enumerate(dnis):
    frec = contar_frecuencias(dni)  # Cuenta las repeticiones de cada dígito
    suma = suma_digitos(dni)        # Suma todos los dígitos del DNI
    print(f"DNI {dni} → Frecuencias: {frec} | Suma: {suma}")

# Evalúa condiciones lógicas entre los conjuntos
print("\n╔═══════════════════════════════════╗")
print("║ Evaluación de condiciones lógicas ║")
print("╚═══════════════════════════════════╝")
for mensaje in evaluar_expresiones_logicas(A, B):
    print("-", mensaje)  # Muestra los mensajes resultantes

# Años de nacimiento (caso de prueba)
anios = [1986, 2004]  # Lista de años de nacimiento predefinida
print("\n╔════════════════════════════════╗")
print("║ Años de nacimiento (de prueba) ║")
print("╚════════════════════════════════╝")
print("Años:", anios)
mensajes_anios, producto = operaciones_anios(anios)  # Llama a la función para obtener mensajes y producto cartesiano
for mensaje in mensajes_anios:
    print("-", mensaje)

# Muestra el producto cartesiano entre año y edad
print("\n╔═════════════════════════════════╗")
print("║ Producto cartesiano (año, edad) ║")
print("╚═════════════════════════════════╝")
for par in producto:
    print(par)

print("\n✅ Fin del programa.\n")  # Mensaje final indicando que el programa ha terminado correctamente
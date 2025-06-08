# 💻 Matemática

**Tecnicatura Universitaria en Programación**
📍 *Universidad Tecnológica Nacional*

## ✨ Estudiantes

- **Nombres:**
  - Daiana Bestabe Peña Juan
  - Claudio Ezequiel Aaron Pereyra
  - Damián Jorge Portillo
- **Comisión:** 19

## **Trabajo Práctico Integrador** - **Conjuntos y lógica**

# 🔢 Análisis de Conjuntos y Lógica a partir de DNIs en Python

Este proyecto integra conceptos de matemática (conjuntos, operaciones, lógica proposicional) y programación en Python. A partir de números de DNI, se generan conjuntos de dígitos únicos y se realizan operaciones clásicas de teoría de conjuntos, además de analizar expresiones lógicas y características de fechas de nacimiento.

---

## 🧠 Objetivo

Automatizar el análisis de conjuntos numéricos derivados de los DNI de los integrantes del grupo, aplicando operaciones matemáticas fundamentales y lógica proposicional. También se incluyen análisis complementarios como suma de dígitos, frecuencias y tratamiento de fechas con producto cartesiano.

---

## 🛠️ Tecnologías Utilizadas

- Python 3.10+
- [datetime](https://docs.python.org/3/library/datetime.html)
- [itertools](https://docs.python.org/3/library/itertools.html)

---

## 📁 Estructura del Proyecto

```
📦tp_conjuntos
 ┣ 📄 TrabajoIntegrador2_Matematica.py
 ┗ 📄 README.md
```

---

## 🚀 Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el script desde la terminal:

```bash
python TrabajoIntegrador2_Matematica.py
```

3. El script solicitará tres DNIs. Puedes presionar *Enter* directamente para utilizar valores de prueba.

---

## 🧮 Funcionalidades del Programa

- Generación de conjuntos con dígitos únicos desde DNIs.
- Cálculo de:
  - Unión, intersección, diferencia y diferencia simétrica entre conjuntos.
  - Frecuencias de aparición de cada dígito por DNI.
  - Suma total de dígitos por DNI.
  - Expresiones lógicas: diversidad numérica y dígitos comunes.
- Evaluación de años de nacimiento:
  - Cantidad de años pares e impares.
  - Nacimientos posteriores a 2000.
  - Presencia de años bisiestos.
  - Producto cartesiano de años y edades.

---

## 📈 Resultados de ejemplo

```
Conjunto A (DNI 36876159): [1, 3, 5, 6, 7, 8, 9]
Conjunto B (DNI 33569007): [0, 3, 5, 6, 7, 9]
Conjunto C (DNI 32238178): [1, 2, 3, 7, 8]

Unión (A ∪ B ∪ C): [0, 1, 2, 3, 5, 6, 7, 8, 9]
Intersección (A ∩ B ∩ C): [3, 7]
...

✔ Todos los conjuntos tienen al menos 5 elementos → Diversidad numérica alta
✔ Dígito(s) compartido(s) en todos: [3, 7]

Años: [1986, 1998, 2004]
✔ Cantidad de nacidos en año par: 3
✔ Al menos uno nació en un año bisiesto → Año especial
```

---

## ✅ Conclusiones

- Las operaciones entre conjuntos permiten identificar intersecciones y diferencias de manera precisa.
- La lógica proposicional aplicada permite validar condiciones útiles como diversidad numérica y valores compartidos.
- El análisis de fechas y producto cartesiano aporta una dimensión adicional de comprensión de datos.

---

## 📚 Referencias

- https://docs.python.org/3/library/datetime.html
- https://docs.python.org/3/library/itertools.html
- https://es.wikipedia.org/wiki/Conjunto_(matem%C3%A1tica)
- https://es.khanacademy.org/math/algebra/x2f8bb11595b61c86:set-theory

import numpy as np

# Ejercicio 1

print("Ejercicio 1 -------------------- ")
print()
print("Punto 1")

# 1).

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

n = 10
print("Factorial de", n, "es:", factorial(n))

print("Punto 2")

#2).

vectores = {}
vectores["V1"] = np.random.randint(1, 11, size=n)
vectores["V2"] = np.random.randint(1, 11, size=n)


vectores["V3"] = np.where(vectores["V1"] < vectores["V2"], 0, 1)

print("\nVectores generados:")
print(vectores)


V1_col = vectores["V1"].reshape(-1, 1)
V2_col = vectores["V2"].reshape(-1, 1)
V3_col = vectores["V3"].reshape(-1, 1)

matriz = np.concatenate((V1_col, V2_col, V3_col), axis=1)

print("\nMatriz final (nx3):")
print(matriz)

# Ejercicio 2

print("Ejercicio 2 -------------------- ")
print()
print("Punto 1")

m = 4
n = 3

# 1).

A = np.zeros((m, n))
print(A)

print("Punto 2")
# 2).

j = 0
while j < n:
    A[:, j] = np.random.randint(-1, 4, size=m)
    j = j + 1

print(A)

A_copia = A.copy()
print("Punto 3")
# 3).

i = 0
while i < m:
    j = 0
    while j < n:
        if A[i, j] < 0:
            A[i, j] = -1
        else:
            A[i, j] = 5
        j = j + 1
    i = i + 1

print(A)
print("Punto 4")
# 4).

for i in range(m):
    for j in range(n):
        if A_copia[i, j] < 0:
            A_copia[i, j] = -1
        else:
            A_copia[i, j] = 5

print(A_copia)

print(np.array_equal(A, A_copia))

print("Ejercicio 3 -------------------- ")
print()
print("Punto 1")

import pandas as pd

import pandas as pd

# 1). crear el df

df = pd.DataFrame({
    "MASA": [71, 45, 50, 60, 61, 84, 55, 60],
    "ESTATURA": [183, 168, 164, 164, 167, 182, 168, 170],
    "GENERO": ["HOMBRE", "HOMBRE", "HOMBRE", "MUJER",
               "HOMBRE", "HOMBRE", "MUJER", "HOMBRE"],
    "ESTRATO": [2, 1, 1, 3, 3, 3, 3, 3],
    "FUMA": ["NO", "NO", "NO", "SI", "SI", "NO", "NO", "SI"]
})

df

# 2). Análisis descriptivo básico de todas las variables

df.info()

df.describe(include="all")

print(df["GENERO"].value_counts())
print(df["FUMA"].value_counts())
print(df["ESTRATO"].value_counts())

# 3). Subconjunto con los primeros 4 estudiantes

subc1 = df.head(4)
subc1
print("sub c 1:")
print(subc1)
# 4). Variables categóricas

subc2 = df[["GENERO", "FUMA"]]
subc2
print("sub c 2:")
print(subc2)
# 5). Variables numéricas

subc3 = df[["MASA", "ESTATURA", "ESTRATO"]]
subc3
print("sub c 3:")
print(subc3)
import random

#Clasificacion de dimensiones
num_ciudades = 3
num_dias_semana = 7
num_semanas = 4

#Generacion matriz con datos aleatorios
temperaturas = [[[random.uniform(-10, 35) for _ in range(num_dias_semana)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

#Matriz
print("Matriz de temperaturas:")
for ciudad in range(num_ciudades):
    print(f"Ciudad {ciudad + 1}:")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}: {temperaturas[ciudad][semana]}")

#Promedio temperaturas ciudad y semana
print("\nPromedio de temperaturas obtenidas por semana y ciudad:")

for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        temperaturas_semana = temperaturas[ciudad][semana]
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)
        print(f"Ciudad {ciudad + 1}, Semana {semana + 1}: Promedio de temperatura = {promedio:.2f}°C")

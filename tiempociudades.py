def temp_promedio(temperaturas):

    promedios = {}

    #Inicializo las variables
    for ciudad, semanas in temperaturas.items():
        total_temperaturas = 0
        num_temperaturas = 0

        #Obtener los datos requeridos
        for semana in semanas:
            total_temperaturas += sum(semana)
            num_temperaturas += len(semana)

        #Sacar el promedio de cada ciudad
        promedio =total_temperaturas / num_temperaturas if num_temperaturas else 0
        promedios[ciudad] =promedio

    return promedios

#Ejemplo
datos_temperaturas = {
    "Madrid": [[18, 25, 21, 19, 23], [22, 25, 27, 17, 13], [18, 21, 26, 20, 19], [21, 26, 28, 19, 24],
               [22, 23, 21, 18, 25]],
    "Lisboa": [[22, 20, 19, 21, 26], [19, 17, 21, 22, 23], [18, 20, 23, 21, 17], [19, 21, 20, 25, 17],
               [16, 20, 19, 26, 22]],
    "Berna": [[14, 18, 20, 9, 13], [11, 17, 12, 10, 14], [9, 12, 11, 14, 13], [13, 17, 10, 11, 16],
              [16, 12, 9, 11, 10]],
    "Nueva York": [[24, 20, 23, 24, 20], [26, 28, 27, 22, 29], [25, 27, 26, 20, 28], [21, 28, 27, 25, 29],
                   [25, 22, 26, 21, 28]]
}

#Usar funcion para la obtencion de resultados
resultados = temp_promedio(datos_temperaturas)
print(resultados)

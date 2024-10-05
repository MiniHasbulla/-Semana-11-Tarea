# Deber archivos 5/10/2024 Amir Puente UEA

#Aqui lo que hago es abrir el archivo en escritura
with open('my_notes.txt', 'w') as file:
    #Luego coloco las lineas personales
    file.write("Ayer vi una película increible llamada Sin City.\n")
    file.write("Esta semana me inscribí en clases de danza artistica.\n")
    file.write("Hoy sabado fue un buen día, ya que salí a correr.\n")
    file.write("Estoy pensando en aprender a tocar la guitarra electrica.\n")
    file.write("Esta semana comprare un libro llamado Papillon.\n")
    file.write("Cuando acabe mi maestria voy a viajar a Suecia.\n")
    file.write("Tengo varios perros, son lindos, pero no dejan de ladrar a los extraños.\n")
    file.write("Tengo que estudiar para los examenes finales.\n")
#Ahora el archivo en lectura
with open('my_notes.txt', 'r') as file:
    #Escojo el archivo línea-línea
    for line in file:
        print(line.strip())  #Cada línea sin el salto de línea extra
#Aqui el archivo se cierra al salir del with

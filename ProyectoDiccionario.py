#Hago el diccionario solicitado
informacion_personal = {
    "nombre": "Daniel Armas",
    "edad": 26,
    "ciudad": "Cuenca",
    "profesion": "Arquitecto"
}
#Modificacion
informacion_personal["ciudad"] = "Quito"
#Nueva clave
informacion_personal["profesion"] = "Futbolista"
#Verificacion
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0988320325"
#Eliminar
if "edad" in informacion_personal:
    del informacion_personal["edad"]
#Mostrar en pantalla
print(informacion_personal)

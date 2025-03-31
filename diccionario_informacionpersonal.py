# Creacion de un diccionario con información personal
informacion_personal = {
    "nombre": "Luis Chavez",
    "edad": 35,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceso y modificacion del valor de la clave "ciudad"
informacion_personal["ciudad"] = "Imbabura"

# Nueva clave-valor ("profesion")
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificacion de la clave "telefono" si existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminacion de la clave "edad" del diccionario
del informacion_personal["edad"]

# Impresion del diccionario final
print("Diccionario final:", informacion_personal)

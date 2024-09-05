nombres = ["Juan", "María", "Pedro", "Juan", "Ana", "Pedro"]

# Lista para almacenar nombres únicos
nombres_unicos = []

for nombre in nombres:
    # Bandera para verificar si el nombre ya está en la lista de nombres únicos
    es_unico = True
    for unico in nombres_unicos:
        if nombre == unico:
            es_unico = False
    # Si el nombre no está en la lista de nombres únicos, agregarlo
    if es_unico:
        nombres_unicos.append(nombre)

# Mostrar los nombres únicos
print(nombres_unicos)

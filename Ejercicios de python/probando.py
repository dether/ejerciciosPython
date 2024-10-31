datos = ["25102024 22.5      CORDOBA OBSERVATORIO"]
#atos = ["012345678901234567890123456789012"] 
""" with open("registro_temperatura365d_smn.txt", "r") as archivo:
    for linea in archivo:
        if linea
        datos.append(linea.strip()) """
for dato in datos:
    cantidad = len(dato)
    temperaturaMax = False
    temperaturaMin = False
    temp_max_str = ""
    temp_min_str = ""
    
    for i in range(9, 14):
        if dato[i] != "":
            temp_max_str = temp_max_str + dato[i]

    if temp_max_str:
        temperaturaMax = float(temp_max_str)  # Convertimos a float el valor numérico
        temperaturaMax = True
    
    for i in range(15, 18):
        if dato[i] != "":
            temp_min_str = temp_min_str + dato[i]
    
    if temp_min_str != "":
        temperaturaMin = float(temp_min_str)
        temperaturaMin = True
        
print(temperaturaMax, temperaturaMin)
        
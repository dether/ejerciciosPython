print("Diseñar un algoritmo para calcular el porcentaje de hombres y de mujeres que hay en un grupo, dados los totales de hombres y de mujeres. ")
hombres = int(input("Ingrese la cantidad de hombres que hay en el grupo: "))
mujeres = int(input("Ingrese la cantidad de mujeres que hay en el grupo: "))
total = hombres + mujeres

print("El porcentaje de hombres que hay en el grupo es de: ", (hombres*100)/total, "%")
print("El porcentaje de mujeres que hay en el grupo es de: ", (mujeres*100)/total, "%")
"""Realizar la función FechaLarga, que recibe una fecha con el formato dd/mm/aaaa y devuelve la 
fecha en formato largo: dia_de_la_semana_en_letras, dd de mes_en_letras de aaaa
Ejemplo: 
print(FechaLarga(“15/07/2023”))
# sábado, 15 de julio de 2023 """

def fechaLarga(fecha: str):
    nuevaFecha = ""
    for i in fecha:
        if i != "/":
            nuevaFecha = nuevaFecha + i
    if len(nuevaFecha) == 8:
        dia = int(nuevaFecha[0] + nuevaFecha[1])
        mes = int(nuevaFecha[2] + nuevaFecha[3])
        anio = int(nuevaFecha[4] + nuevaFecha[5] + nuevaFecha[6] + nuevaFecha[7])
    elif len(nuevaFecha) == 7:
        dia = int(nuevaFecha[0] + nuevaFecha[1])
        mes = int(nuevaFecha[2])
        anio = int(nuevaFecha[3] + nuevaFecha[4] + nuevaFecha[5] + nuevaFecha[6])
    """ print(f"fecha: {dia}/{mes}/{anio}") """
    #Fórmula de Zeller para determinar el día (lunes, martes.....)
    #h = (dia + (13 * (mes + 1)) // (5) + K + (K // 4) + (J // 4) - 2 * J) % 7
    calculandoMes = mes
    calculandoAnio = anio
    if mes < 3:
        calculandoMes = calculandoMes + 12
        calculandoAnio = anio - 1

    K = calculandoAnio % 100 # K es el año dentro del siglo
    J = calculandoAnio // 100 # J es el siglo

    h = (dia + (13 * (calculandoMes + 1)) // 5 + K + (K // 4) + ( J // 4) - 2 * J) % 7

    diasSemana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    resultado = f"{diasSemana[h]}, {dia} de {meses[mes - 1]} de {anio}"
    return resultado

asd = fechaLarga("17/1/1996")
print(asd)
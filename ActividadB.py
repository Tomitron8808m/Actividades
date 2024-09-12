'''
Ejercicio 7:
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente.
Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.
Ejercicio 9:
Genere un paquete con ambos módulos.
Ejercicio 10:
Subir a github el paquete.
'''
#7
def ventas_nacionales(precio_ventas_nacionales, iva=21):

    return precio_ventas_nacionales * (1 + (iva / 100))

def exportaciones(precio_exportaciones, retenciones=15):

    return precio_exportaciones * (1 - (retenciones / 100))

def impuestos(precio_exportaciones, precio_ventas_nacionales, iva=21, retenciones=15):

    ventas_iva = ventas_nacionales(precio_ventas_nacionales, iva)
    exportaciones_retenciones = exportaciones(precio_exportaciones, retenciones)
    return ventas_iva + exportaciones_retenciones

#8

def calcular_salario(horas_trabajadas, antiguedad, tarifa_hora=10):

    incremento_antiguedad = 1 + (antiguedad * 0.03)  # 3% por cada año
    salario = horas_trabajadas * tarifa_hora * incremento_antiguedad
    return salario

def calcular_productividad(artefactos_producidos, horas_trabajadas):

    if horas_trabajadas == 0:
        return 0
    return artefactos_producidos / horas_trabajadas

def reporte_empleado(nombre, edad, horas_trabajadas, antiguedad, artefactos_producidos):


    salario = calcular_salario(horas_trabajadas, antiguedad)
    productividad = calcular_productividad(artefactos_producidos, horas_trabajadas)
    
    reporte = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario,
        "Productividad": productividad,
        "Horas Trabajadas": horas_trabajadas,
        "Antigüedad": antiguedad,
        "Artefactos Producidos": artefactos_producidos
    }
    
    return reporte

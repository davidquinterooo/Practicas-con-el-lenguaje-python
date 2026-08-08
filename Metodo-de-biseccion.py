"""
El método de bisección, también conocido como método de búsqueda binaria, utiliza una búsqueda binaria para encontrar las raíces de una función de valor real. Funciona reduciendo un intervalo donde se encuentra la raíz cuadrada hasta que converge a un valor dentro de una tolerancia específica.

Por ejemplo, si la tolerancia es 0,01, el método de bisección seguirá reduciendo a la mitad el intervalo hasta que la diferencia entre los límites superior e inferior sea menor o igual a 0,01.

En este laboratorio, implementará una función que utiliza el método de bisección para encontrar la raíz cuadrada de un número.

Objetivo: Cumpla las historias de los usuarios a continuación y obtenga todas las pruebas para aprobar y completar el laboratorio.

Historias de usuarios:

Deberías definir una función llamada square_root_bisection cu trei parametri:

El número para el que desea encontrar la raíz cuadrada.
La tolerancia es el margen de error aceptable para el resultado. Debe establecer un valor de tolerancia predeterminado.
El número máximo de iteraciones a realizar. Debe establecer un número predeterminado de iteraciones.
El square_root_bisection funcția ar trebui:

Levantar un Error de valor con el mensaje La raíz cuadrada del número negativo no está definida en números reales si el número pasado a la función es negativo.
Para números 0 y 1, imprime el mensaje: La raíz cuadrada de [número] es [número] y devuelve el número mismo como raíz cuadrada.
Para cualquier otro número positivo, imprima la raíz cuadrada aproximada con el mensaje: La raíz cuadrada de [square_target] es aproximadamente [raíz] y devuelva el valor raíz calculado.
Si ningún valor cumple con la condición de tolerancia, imprima un mensaje de falla: No se pudo converger dentro de las iteraciones [máximas] y regresa Ninguno.
Nota: No puedes importar ningún módulo para este laboratorio.
"""

def square_root_bisection(num, tolerancia=1e-7, max_iteraciones=100):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    elif num == 0 or num == 1:
        print(f'The square root of {num} is {num}')
        return num
    
    low = 0
    high = max(1.0, float(num))
    root = None

    for _ in range(max_iteraciones):
        mid = (low + high) / 2
        if abs(high - low) < tolerancia:
            root = mid
            break
        if mid ** 2 < num:
            low = mid
        else:
            high = mid
    if root is not None:
        print(f'The square root of {num} is approximately {root}')
        return root
    else:
        print(f"Failed to converge within {max_iteraciones} iterations")
        return None

square_root_bisection(0.001, 1e-7, 50)
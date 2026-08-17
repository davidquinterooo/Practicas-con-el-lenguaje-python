"""
Implementación del algoritmo de Luhn
El algoritmo de Luhn, también conocido como algoritmo "módulo 10" o "mod 10", es una fórmula de suma de verificación sencilla que se utiliza para validar diversos números de identificación, como los de tarjetas de crédito. Estos son los pasos para validar un número mediante el algoritmo de Luhn:

Comenzando desde la derecha y excluyendo el último dígito (el dígito de control), duplique el valor de cada dígito alterno.

Si el resultado de duplicar un dígito es mayor que 9, sume los dígitos para obtener un solo dígito. También puede restar 9 al resultado.

Sume todos los dígitos, incluyendo el dígito de control.

Si la suma de todos los dígitos es un múltiplo de 10, el número es válido; de lo contrario, no lo es.
Por ejemplo, consideremos el número 453914881. Los pasos para validarlo mediante el algoritmo de Luhn son:

Número de cuenta: 4 5 3 9 1 4 8 8 1
Duplicar cada dígito alterno: 4 10 3 18 1 8 8 16 1
Sumar los dígitos de dos caracteres: 4 1 3 9 1 8 8 7 1
Luego, sumar todos los números: 4 + 1 + 3 + 9 + 1 + 8 + 8 + 7 + 1 = 42.
Como 42 no es múltiplo de 10, el número es inválido.

En este laboratorio, crearás un validador de tarjetas de crédito utilizando el algoritmo de Luhn.

Objetivo: Cumplir con las historias de usuario que se detallan a continuación y lograr que todas las pruebas se superen para completar el laboratorio.

Historias de usuario:

Debes definir una función llamada `verify_card_number` que reciba una cadena de dígitos (que representa un número de tarjeta) y verifique su validez según el algoritmo de Luhn.

Dentro de la función `verify_card_number`:

Debes gestionar los guiones o espacios que pueda contener el número de tarjeta.

Devuelve `VALID!` si el número de tarjeta es válido; de lo contrario, devuelve `INVALID!`.

Al finalizar el proyecto, deberías ver los siguientes mensajes, según el número de entrada:
"""
def verify_card_number(card_number):
    clean_number = str(card_number).replace('-', '').replace(' ', '')
    
    digits = [int(d) for d in clean_number]
    total_sum = 0
    
    for index, digit in enumerate(digits[::-1]):
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        total_sum += digit

    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'


if __name__ == '__main__':
    print(verify_card_number('453914881'))      # Retorna: INVALID!
    print(verify_card_number('4539-1488-9'))    # Retorna: INVALID!
    print(verify_card_number('4539 1488 8'))    # Retorna: VALID!
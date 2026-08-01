# Cree una aplicación económica #
En este laboratorio, creará una aplicación de presupuesto simple que rastrea el 
gasto en diferentes categorías y puede mostrar el porcentaje de gasto relativo en 
un gráfico.

**Objetivo**: Cumpla las historias de los usuarios a continuación y obtenga todas 
las pruebas para aprobar y completar el laboratorio.

**Historias de usuarios:**

1. Deberías tener un Categoría clase que acepta un nombre como argumento.

2. El Categoría la clase debe tener un atributo de instancia libro mayor esa es una 
lista y contiene la lista de transacciones.

3. El Categoría la clase debe tener los siguientes métodos:

    - A depósito método que acepta una cantidad y una descripción opcional. Si no se 
    proporciona ninguna descripción, se debe establecer de forma predeterminada una 
    cadena vacía. El método debe agregar un objeto al libro mayor lista en forma 
    de {'cantidad': cantidad, 'descripción': descripción}.

    - A retirar método que acepta una cantidad y una descripción opcional (predeterminada 
    en una cadena vacía). El método debería almacenarse libro mayor el monto pasó como un 
    número negativo y debe devolverse Verdadero si la retirada tuvo éxito y Falso de lo 
    contrario.

    - A obtener_equilibrio método que devuelve el saldo de la categoría actual según libro 
    mayor.
    
    - A transferir método que acepta una cantidad y otra Categoría instancia, retira el monto 
    con descripción Transferir a [Destino], lo deposita en la otra categoría con descripción 
    Transferir desde [Fuente], donde [Destino] y [Fuente] debe reemplazarse por el nombre de 
    las categorías de destino y origen. El método debería regresar Verdadero cuando la 
    transferencia sea exitosa, y Falso de lo contrario.
    
    - A cheque_fondos método que acepta una cantidad y devuelve Falso si excede el saldo o 
    Verdadero de lo contrario. Este método debe ser utilizado por ambos retirar y transferir 
    métodos.

4. Cuando un Categoría el objeto está impreso, debería:

    - Muestra una línea de título de 30 caracteres con el nombre de la categoría centrado entre 
    ellos * personajes.
    
    - Enumere cada uno libro mayor entrada con hasta 23 caracteres de su descripción alineados 
    a la izquierda y la cantidad alineada a la derecha (dos decimales, máximo 7 caracteres).
    
    - Mostrar una línea final Total: [saldo], donde [equilibrio] debería sustituirse por el total 
    de la categoría.
    
    **A continuación se muestra un uso de ejemplo:**
```
comida = Categoría('Alimento')
comida.depósito(1000, 'depósito inicial')
comida.retirar(10.15, 'comestibles')
comida.retirar(15,89, 'restaurante y más comida de postre')
ropa = Categoría('Ropa')
comida.transferir(50, ropa)
imprimir(comida)
```
Y aquí hay un ejemplo del resultado:
```
*************Comida*************
depósito inicial        1000,00
comestibles               -10.15
restaurante y más foo -15,89
Transferir a la ropa    -50,00
Total: 923,96
```

5. Deberías tener una función fuera del Categoría clase nombrada create_spend_chart(categorías) 
eso toma una lista de categorías y devuelve una cadena de gráfico de barras. Para construir 
el gráfico:

    - Comience con el título Porcentaje gastado por categoría.
    
    - Calcule porcentajes únicamente de retiros y no de depósitos. El porcentaje debe ser el 
    porcentaje del monto gastado para cada categoría sobre el total gastado para todas las 
    categorías (redondeado al 10 más cercano).
    
    - Etiquete el eje y desde 100 hasta 0 en pasos de 10.
    
    - Usar o personajes para los bares.
    
    - Incluya una línea horizontal dos espacios más allá de la última barra.
    
    - Escriba los nombres de las categorías verticalmente debajo de la barra.
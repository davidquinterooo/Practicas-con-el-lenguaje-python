"""
Cree una calculadora de área poligonal
En este proyecto, utilizará programación orientada a objetos para crear un Rectángulo clase y a Cuadrado clase. El Cuadrado la clase debe ser una subclase de Rectángulo y heredar sus métodos y atributos.

Objetivo: Cumpla las historias de los usuarios a continuación y obtenga todas las pruebas para aprobar y completar el laboratorio.

Historias de usuarios:

Deberías crear un Rectángulo clase.

Cuando un Rectángulo se crea el objeto, se debe inicializar con ancho y altura atributos. La clase también debe contener los siguientes métodos:

establecer_ancho: Establece el ancho del rectángulo.
establecer_altura: Establece la altura del rectángulo.
get_area: Área de devoluciones ( ancho×altura).
obtener_perímetro: Devuelve perímetro  2(ancho+altura)
 .
get_diagonal: Devuelve diagonal  ancho2+altura2−−−−−−−−−−−−−−√
 .
obtener_imagen: Devuelve una cadena que representa la forma usando líneas de *. El número de líneas debe ser igual a la altura y al número de * en cada línea debe ser igual al ancho. Debería haber una nueva línea (\n) al final de cada línea. Si el ancho o alto es mayor que 50, esto debería devolver la cadena: Demasiado grande para la imagen..
get_amount_inside: Toma otra forma (cuadrada o rectángulo) como argumento. Devuelve el número de veces que la forma pasada podría caber dentro de la forma (sin rotaciones). Por ejemplo, un rectángulo con un ancho de 4 y una altura de 8 podría caber en dos cuadrados con lados de 4.
Si una instancia de a Rectángulo se representa como una cadena, debería verse como: Rectángulo(ancho=5, alto=10).

Deberías crear un Cuadrado clase que subclases Rectángulo.

Cuando un Cuadrado se crea el objeto, se debe inicializar con una longitud de un solo lado. El __init__ el método debe almacenar la longitud del lado en ambos ancho y altura atributos del Rectángulo clase.

El Cuadrado la clase debe contener los siguientes métodos:

establecer_ancho: Anula el establecer_ancho método del Rectángulo clase. Debe ajustar el ancho y el alto al largo lateral.
establecer_altura: Anula el establecer_altura método del Rectángulo clase. Debe ajustar el ancho y el alto al largo lateral.
set_side: Establece la altura y el ancho del cuadrado igual a la longitud del lado.
El Cuadrado la clase debería poder acceder al Rectángulo métodos de clase.

Si una instancia de a Cuadrado se representa como una cadena, debería verse como: Cuadrado (lado=9). """

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)
    
    def get_diagonal(self):
        return math.sqrt(self.width**2+self.height**2)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = "*" * self.width + "\n"
        return line * self.height
    
    def get_amount_inside(self, shape) -> int:
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height

        return fit_width * fit_height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
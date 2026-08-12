"""
Construye una mesa hash
En este laboratorio, construirás una tabla hash desde cero. Una tabla hash es una estructura de datos que almacena pares clave-valor. Una tabla hash funciona tomando la clave como entrada y luego modificando esta clave según una función hash específica.

Para los fines de este laboratorio, la función hash será simple: sumará los valores Unicode de cada carácter en la clave. Luego, el valor hash se utilizará como clave real para almacenar el valor asociado. El mismo valor hash también se usaría para recuperar y eliminar el valor asociado con la clave.

Objetivo: Cumpla las historias de los usuarios a continuación y obtenga todas las pruebas para aprobar y completar el laboratorio.

Historias de usuarios:

Deberías definir una clase llamada Mesa hash con un colección atributo inicializado a un diccionario vacío cuando una nueva instancia de Mesa hash es creado. El colección el diccionario debe almacenar pares clave-valor según el valor hash de la clave.

El Mesa hash la clase debe tener cuatro métodos de instancia: hachís, agregar, quitar, și buscar.

El hachís método ar trebui:

Tome una cadena como parámetro.
Devuelve un valor hash calculado como la suma de los valores Unicode (ASCII) de cada carácter de la cadena. Puedes usar el ord función para este cálculo.
El agregar método ar trebui:

Tome dos argumentos que representen un par clave-valor y calcule el hash de la clave.
Utilice el valor hash calculado como clave para almacenar un diccionario que contenga el par clave-valor dentro del colección diccionario.
Si varias claves producen el mismo valor hash, sus pares clave-valor deben almacenarse en el diccionario anidado existente con el mismo valor hash.
El quitar método ar trebui:

Tome una clave como argumento y calcule su hash.
Confirme si la clave existe en la colección.
Elimine el par clave-valor correspondiente de la tabla hash.
Si la clave no existe en la colección, no debe generar ningún error ni eliminar nada.
El buscar método ar trebui:

Tomemos como argumento una clave.
Calcule el hash de la clave y devuelva el valor correspondiente almacenado dentro de la tabla hash.
Si la clave no existe en la colección, deberá devolverse Ninguno.
"""

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        self.collection[hash_key][key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None
# Motor de Cálculo de Descuentos Dinámicos (Strategy Pattern in Python)

Este proyecto implementa un sistema flexible para calcular el precio final 
de un producto aplicando el mejor descuento disponible según el perfil del 
usuario y las condiciones del producto. 

El objetivo principal es demostrar el uso del **Patrón de Diseño Strategy (Estrategia)** 
y los principios de diseño de software orientados a objetos en Python.

---

## Características Principales

- **Diseño Desacoplado:** Uso de Clases Abstractas (`ABC`) para definir contratos claros 
en las estrategias de descuento.
- **Extensibilidad (Principio Open/Closed):** Permite añadir nuevos tipos de descuentos 
sin modificar la lógica interna del motor principal (`DiscountEngine`).
- **Filtrado Inteligente:** Cada descuento valida autónomamente si es aplicable mediante 
reglas de negocio (`is_applicable`).
- **Optimización para el Usuario:** Evalúa todas las estrategias válidas y garantiza 
seleccionar siempre el precio más bajo (`min`).
- **Tipado Estático (*Type Hints*):** Métodos anotados con tipos de datos para mayor 
legibilidad y prevención de errores.

---

## Estructura del Código

1. **`Product`**: Clase modelo que representa un artículo con nombre y precio base.
2. **`DiscountStrategy` (Interfaz Abstracta)**: Declara los métodos obligatorios:
   - `is_applicable(product, user_tier)`: Evalúa si el descuento es válido.
   - `apply_discount(product)`: Aplica el cálculo y retorna el precio resultante.
3. **Estrategias Concretas**:
   - `PercentageDiscount`: Descuento porcentual (válido si el porcentaje es $\le 70\%$).
   - `FixedAmountDiscount`: Descuento de monto fijo en dinero (válido si no excede el 10% del precio del producto).
   - `PremiumUserDiscount`: Descuento exclusivo del 20% para usuarios de nivel *Premium*.
4. **`DiscountEngine`**: Motor principal que itera sobre la lista de estrategias registradas, filtra las aplicables y calcula la mejor oferta.

---

## Ejemplo de Uso

```python
# Definición de producto y usuario
product = Product('Wireless Mouse', 50.0)
user_tier = 'Premium'

# Registro de estrategias disponibles
strategies = [
    PercentageDiscount(10),     # 10% de descuento ($45.00)
    FixedAmountDiscount(5),      # $5.00 de descuento ($45.00)
    PremiumUserDiscount()        # 20% por ser Premium ($40.00)
]

# Inicialización del motor y cálculo
engine = DiscountEngine(strategies)
best_price = engine.calculate_best_price(product, user_tier)

print(f'Best price for {product.name} for {user_tier} user: ${best_price:.2f}')
# Salida: Best price for Wireless Mouse for Premium user: $40.00
class Category:
    def __init__(self,name): 
        self.name = name
        self.ledger = []
    

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Retorna False si el monto supera el saldo actual, True en caso contrario
        return amount <= self.get_balance()

    def __str__(self):
        output = f'{self.name:*^30}\n'
        # 2. Filas de transacciones
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            output += f"{desc}{amount}\n"

        # 3. Saldo final
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    # Paso 1: Totales gastados
    spent = [sum(-item["amount"] for item in cat.ledger if item["amount"] < 0) for cat in categories]
    total_spent = sum(spent)

    # Paso 2: Porcentajes redondeados hacia abajo a la decena
    percentages = [
        int((s / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0
        for s in spent
    ]

    # Paso 3: Título y eje Y con barras
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Paso 4: Línea horizontal
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Paso 5: Nombres verticales
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  " if i < len(name) else "   "
        if i < max_len - 1:
            chart += "\n"

    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.50, 't-shirt')

# 1. Representación en texto de la categoría 'Food'
print("=== RECIBO DE CATEGORÍA ===")
print(food)

print("\n" + "="*30 + "\n")

# 2. Gráfico de gastos comparando 'Food' y 'Clothing'
print("=== GRÁFICO DE GASTOS ===")
print(create_spend_chart([food, clothing]))
# billing_logic.py

class BillingSystem:
    def calculate_total(self, items):
        total = 0
        for item in items:
            total += item['price'] * item['quantity']
        return total



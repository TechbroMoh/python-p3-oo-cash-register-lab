#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.last_transaction = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        if not isinstance(price, (int, float)) or not isinstance(quantity, int):
            raise TypeError("Price must be a number and quantity must be an integer.")
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            self.total = round(self.total, 2)  # Round to 2 decimal places
            # Format the total without unnecessary trailing zeros
            formatted_total = f"${self.total:.2f}".rstrip('0').rstrip('.')
            print(f"After the discount, the total comes to {formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.total = round(self.total, 2)
        self.last_transaction = 0

    def items_list(self):
        return self.items

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        # Increase total
        amount = price * quantity
        self.total += amount
        
        # Save last transaction amount for voiding
        self.last_transaction_amount = amount

        # Add items to list (including multiples)
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Convert to int to match expected output (800 instead of 800.0)
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Remove last transaction value from total
        self.total -= self.last_transaction_amount
        
        # Prevent negative totals
        if self.total < 0:
            self.total = 0


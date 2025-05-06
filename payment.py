from datetime import datetime

class Payment:
    # Initialize a transaction or payment with a specified amount and optional date
    def __init__(self, value, payment_date=None):
        self.value = value
        self.payment_date = payment_date if payment_date else datetime.now().strftime("%Y-%m-%d")

    # Reminders: Notify user of upcoming or due transaction
    def notify_due(self):
        print("Notice: Please complete your transaction at your earliest convenience.")

    # Penalties: Add a late charge to the transaction
    def add_late_fee(self, fee):
        self.value += fee
        print(f"Late fee of ${fee:,.2f} added. Updated total: ${self.value:,.2f}")


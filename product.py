class Product:
    # Set up a new insurance product with title and cost; default status is set to enabled
    def __init__(self, title, cost):
        self.title = title              # Name of the product
        self.cost = cost                # Pricing information
        self.is_active = True           # Product is initially active

    # Adjust the current cost of the product
    def change_cost(self, revised_cost):
        self.cost = revised_cost
        print(f"Updated cost for {self.title}: ${self.cost}")

    # Mark the product as temporarily inactive
    def deactivate(self):
        self.is_active = False
        print(f"{self.title} has been marked as inactive.")

    # Bring the product back to active use
    def activate(self):
        self.is_active = True
        print(f"{self.title} is now active again.")

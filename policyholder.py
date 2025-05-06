class Policyholder:
    # Initialize a client with their full name and ID; default status is set to active
    def __init__(self, full_name, client_id):
        self.full_name = full_name
        self.client_id = client_id
        self.current_status = "Active"
        self.covered_products = []
        self.payment_records = []

    # Register: Confirm client registration with a welcome message
    def enroll(self):
        print(f"{self.full_name} (Client ID: {self.client_id}) has been successfully enrolled.")

    # Suspend: Mark the client as temporarily suspended
    def deactivate(self):
        self.current_status = "Suspended"

    # Restore: Restore client's account to active status
    def reactivate(self):
        self.current_status = "Active"

    # Link an insurance product to the client
    def assign_product(self, policy_product):
        self.covered_products.append(policy_product)

    # Record a new payment made by the client
    def log_payment(self, transaction):
        self.payment_records.append(transaction)

    # Display full details of the client including associated products and payment history
    def show_profile(self):
        print(f"\nClient: {self.full_name} (ID: {self.client_id})")
        print(f"Status: {self.current_status}")

        print("Subscribed Products:")
        for item in self.covered_products:
            print(f" - {item.title} (${item.cost}) | Active: {item.is_active}")

        print("Transaction History:")
        for txn in self.payment_records:
            print(f" - ${txn.value} made on {txn.payment_date}")

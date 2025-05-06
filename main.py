from policyholder import Policyholder
from product import Product
from payment import Payment

# Instantiate a policy product
retirement_plan = Product("Retirement Plan", 50000)

# Update the product's cost and deactivate it
retirement_plan.change_cost(72000)
retirement_plan.deactivate()

# Activate it again later
retirement_plan.activate()

# Register two new policyholders
alice = Policyholder("Alice Onyeka", "PL101")
alice.enroll()

ben = Policyholder("Ben Ajayi", "PL102")
ben.enroll()

# Record payments with reminders and penalties
pay_alice = Payment(65000)
pay_alice.notify_due()
pay_alice.add_late_fee(10000)

pay_ben = Payment(12000)

# Associate product and payment records to policyholders
alice.assign_product(retirement_plan)
alice.log_payment(pay_alice)

ben.assign_product(retirement_plan)
ben.log_payment(pay_ben)

# Temporarily disable and re-enable Alice’s policy
alice.deactivate()
alice.reactivate()

# Show each policyholder's information
alice.show_profile()
ben.show_profile()

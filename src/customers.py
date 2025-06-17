class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.account_numbers = []

    def add_account(self, account_number):
        if account_number not in self.account_numbers:
            self.account_numbers.append(account_number)

    def remove_account(self, account_number):
        if account_number in self.account_numbers:
            self.account_numbers.remove(account_number)

    def display_details(self):
        return {
            "name": self.name,
            "customer_id": self.customer_id,
            "account_numbers": self.account_numbers
        }

    def to_dict(self):
        return {
            "name": self.name,
            "customer_id": self.customer_id,
            "account_numbers": self.account_numbers
        }
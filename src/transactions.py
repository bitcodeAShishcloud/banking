class Bank:
    def __init__(self):
        # Initialize the bank with an empty dictionary of customers
        self.customers = {}
    
    def add_customer(self, customer):
        # Add a new customer if they don't already exist
        if customer.id not in self.customers:
            self.customers[customer.id] = customer
            print(f"Customer {customer.name} added successfully.")
        else:
            print("Customer already exists.")
    
    def remove_customer(self, customer_id):
        # Remove a customer by their ID if they exist
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer with ID {customer_id} removed successfully.")
        else:
            print("Customer not found.")
    
    def create_account(self, customer_id, account_type, initial_balance=0):
        # Create a new account (savings or checking) for a customer
        if customer_id in self.customers:
            account = None
            if account_type == 'savings':
                account = SavingsAccount(initial_balance)
            elif account_type == 'checking':
                account = CheckingAccount(initial_balance)
            if account:
                self.customers[customer_id].add_account(account)
                print(f"{account_type.capitalize()} account created for customer {customer_id}.")
        else:
            print("Customer not found.")
    
    def deposit(self, customer_id, account_id, amount):
        # Deposit an amount into a customer's account
        if customer_id in self.customers:
            account = self.customers[customer_id].get_account(account_id)
            if account:
                account.deposit(amount)
                print(f"Deposited {amount} to account {account_id}.")
            else:
                print("Account not found.")
        else:
            print("Customer not found.")
    
    def withdraw(self, customer_id, account_id, amount):
        # Withdraw an amount from a customer's account
        if customer_id in self.customers:
            account = self.customers[customer_id].get_account(account_id)
            if account:
                account.withdraw(amount)
                print(f"Withdrew {amount} from account {account_id}.")
            else:
                print("Account not found.")
        else:
            print("Customer not found.")
    
    def transfer(self, from_customer_id, from_account_id, to_customer_id, to_account_id, amount):
        # Transfer an amount from one customer's account to another's
        if from_customer_id in self.customers and to_customer_id in self.customers:
            from_account = self.customers[from_customer_id].get_account(from_account_id)
            to_account = self.customers[to_customer_id].get_account(to_account_id)
            if from_account and to_account:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred {amount} from account {from_account_id} to account {to_account_id}.")
            else:
                print("One of the accounts not found.")
        else:
            print("One of the customers not found.")
    
    def save_data(self, filename):
        # Implementation for saving data to a file
        pass
    
    def load_data(self, filename):
        # Implementation for loading data from a file
        pass
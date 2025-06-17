class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_details(self):
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'balance': self.balance
        }

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'balance': self.balance
        }


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False
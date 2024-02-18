from account import Account
from customer import Customer


class BankSystem:
    def __init__(self):
        self.customers = []

    def open_account(self):
        name = input("Enter customer name: ")
        customer_type = input("Enter customer type (Private/Business): ").lower()
        initial_balance = float(input("Enter initial balance: "))

        customer = Customer(name)
        account = None
        if customer_type == 'private':
            account = Account(initial_balance)
        elif customer_type == 'business':
            account = Account(initial_balance, is_business=True)
        else:
            print("Invalid customer type.")
            return

        customer.set_account(account)
        self.customers.append(customer)
        print("Account opened successfully.")

    def close_account(self):
        customer_name = input("Enter customer name: ")
        for customer in self.customers:
            if customer.name == customer_name:
                self.customers.remove(customer)
                print(f"Account for {customer_name} closed successfully.")
                return
        print("Customer not found.")

    def deposit_money(self):
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter amount to deposit: "))
        for customer in self.customers:
            if customer.name == customer_name:
                customer.account.balance += amount
                print(f"{amount} deposited successfully to {customer_name}'s account.")
                return
        print("Customer not found.")

    def withdraw_money(self):
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter amount to withdraw: "))
        for customer in self.customers:
            if customer.name == customer_name:
                if customer.account.balance >= amount:
                    customer.account.balance -= amount
                    print(f"{amount} withdrawn successfully from {customer_name}'s account.")
                else:
                    print("Insufficient funds.")
                return
        print("Customer not found.")

    def view_account_status(self):
        customer_name = input("Enter customer name: ")
        for customer in self.customers:
            if customer.name == customer_name:
                print(f"Customer Name: {customer.name}")
                print(f"Account Balance: {customer.account.balance}")
                return
        print("Customer not found.")

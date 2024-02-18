from bank_system import BankSystem


def main():
    bank_system = BankSystem()
    while True:
        print("1. Open Account")
        print("2. Close Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Account Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bank_system.open_account()
        elif choice == '2':
            bank_system.close_account()
        elif choice == '3':
            bank_system.deposit_money()
        elif choice == '4':
            bank_system.withdraw_money()
        elif choice == '5':
            bank_system.view_account_status()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

def main():
    from transactions import Bank

    bank = Bank()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Create Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Display Customer Details")
        print("8. Exit")

        choice = input("Please select an option (1-8): ")

        if choice == '1':
            bank.add_customer()
        elif choice == '2':
            bank.remove_customer()
        elif choice == '3':
            bank.create_account()
        elif choice == '4':
            bank.deposit()
        elif choice == '5':
            bank.withdraw()
        elif choice == '6':
            bank.transfer()
        elif choice == '7':
            bank.display_customer_details()
        elif choice == '8':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
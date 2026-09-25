customer = {
    "name": "Ali Nawaz",
    "account": "XXXX1234",
    "pin": "1234"
}

balance = 10000
withdrawn_today = 0


def check_balance():
    print("\n----- BALANCE -----")
    print("Account:", customer["account"])
    print("Available Balance: ₹", balance)


def deposit_money():
    global balance

    print("\n----- DEPOSIT -----")
    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Invalid amount.")
        return

    balance += amount

    print("Amount deposited successfully.")
    print("New Balance: ₹", balance)


def withdraw_money():
    global balance, withdrawn_today

    print("\n----- WITHDRAW -----")
    amount = int(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount.")

    elif amount % 100 != 0:
        print("Amount must be a multiple of ₹100.")

    elif amount > 5000:
        print("Maximum withdrawal per transaction is ₹5000.")

    elif withdrawn_today + amount > 25000:
        print("Daily withdrawal limit exceeded.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        print("Processing money...")

        balance -= amount
        withdrawn_today += amount

        print("\n----- RECEIPT -----")
        print("Account:", customer["account"])
        print("Transaction: Cash Withdrawal")
        print("Amount: ₹", amount)
        print("Remaining Balance: ₹", balance)
        print("-------------------")
        print("Please collect your cash.")


def daily_limit():
    print("\n----- DAILY LIMIT -----")
    print("Daily Limit: ₹25000")
    print("Withdrawn Today: ₹", withdrawn_today)
    print("Remaining Limit: ₹", 25000 - withdrawn_today)


def change_pin():
    old_pin = input("Enter current PIN: ")

    if old_pin != customer["pin"]:
        print("Incorrect PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ")

    if new_pin == confirm_pin:
        customer["pin"] = new_pin
        print("PIN changed successfully.")
    else:
        print("PINs do not match.")


def authenticate():
    attempts = 0

    while attempts < 3:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == customer["pin"]:
            print("PIN verified successfully.")
            return True

        attempts += 1
        print("Incorrect PIN.")

        if attempts < 3:
            print("Attempts remaining:", 3 - attempts)

    return False


print("================================")
print("        WELCOME TO ATM")
print("================================")

print("Insert your card...")
input("Press Enter to continue: ")

print("\nReading card details...")
print("Card detected.")
print("Welcome,", customer["name"])
print("Account ending:", customer["account"][-4:])

if authenticate():

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Daily Limit")
        print("5. Change PIN")
        print("6. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            daily_limit()

        elif choice == "5":
            change_pin()

        elif choice == "6":
            print("\nThank you for using our ATM.")
            print("Please take your card.")
            print("Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("\nMaximum PIN attempts reached.")
    print("Your card has been blocked.")

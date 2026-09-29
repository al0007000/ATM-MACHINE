# atm project
name = "Ali Nawaz"
card = "XXXX1234"
pin = "1234"

bal = 10000
wd_today = 0
limit = 25000

print("Welcome to the ATM")
input("Insert card and press enter")
print("Hello", name, "card ending", card[-4:])

# pin check
ok = False
tries = 3
while tries > 0:
    p = input("Enter PIN: ")
    if p == pin:
        ok = True
        break
    tries -= 1
    print("Wrong PIN,", tries, "tries left")

if ok:
    while True:
        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Daily limit")
        print("5. Exit")
        ch = input("Choice: ")

        if ch == "1":
            print("Balance:", bal)

        elif ch == "2":
            amt = int(input("Deposit amount: "))
            if amt <= 0:
                print("Invalid amount")
            else:
                bal += amt
                print("Deposited. New balance:", bal)

        elif ch == "3":
            amt = int(input("Withdraw amount: "))
            if amt <= 0:
                print("Invalid amount")
            elif amt % 100 != 0:
                print("Enter multiples of 100")
            elif amt > 5000:
                print("Max 5000 per transaction")
            elif wd_today + amt > limit:
                print("Daily limit reached")
            elif amt > bal:
                print("Not enough balance")
            else:
                bal -= amt
                wd_today += amt
                print("Take your cash:", amt)
                print("Balance left:", bal)

        elif ch == "4":
            print("Withdrawn today:", wd_today)
            print("Remaining:", limit - wd_today)

        elif ch == "5":
            print("Thank you, take your card")
            break

        else:
            print("Wrong choice")
else:
    print("Too many wrong attempts, card blocked")

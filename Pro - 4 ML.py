pin = 1234
bal = 10000
p = int(input("PIN: "))
if p == pin:
    amt = int(input("Amount: "))
    if amt <= bal:
        print("Balance:", bal - amt)
    else:
        print("Insufficient Balance")
else:
    print("Wrong PIN")

seats = int(input("Seats: "))
price = 200
total = seats*price
if seats>=5:
    total *= 0.9
print("Total:", total)

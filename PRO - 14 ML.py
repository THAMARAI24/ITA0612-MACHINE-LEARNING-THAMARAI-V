att = int(input("Classes Attended: "))
total = int(input("Total Classes: "))
per = att/total*100
print(per)
print("Eligible" if per>=75 else "Not Eligible")

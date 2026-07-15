fare = 500
age = int(input("Age: "))
if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7
print("Fare:", fare)

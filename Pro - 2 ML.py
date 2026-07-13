salary = float(input("Enter Basic Salary: "))

pf = salary * 0.12
tax = salary * 0.10
net = salary - (pf + tax)

print("Gross Salary:", salary)
print("PF:", pf)
print("Tax:", tax)
print("Net Salary:", net)

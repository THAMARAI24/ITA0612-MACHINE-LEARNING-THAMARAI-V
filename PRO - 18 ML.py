age = int(input("Age: "))
wt = int(input("Weight: "))
hb = float(input("HB: "))
if age>=18 and wt>=50 and hb>=12.5:
    print("Eligible")
else:
    print("Not Eligible")

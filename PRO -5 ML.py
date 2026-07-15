amt = float(input("Amount: "))
dis = amt * 0.10 if amt > 5000 else 0
gst = (amt - dis) * 0.18
print("Total Bill:", amt - dis + gst)

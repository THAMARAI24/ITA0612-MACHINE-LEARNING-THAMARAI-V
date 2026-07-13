total = 0

for i in range(5):
    total += int(input("Enter marks: "))

avg = total / 5

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "D"

print("Total:", total)
print("Average:", avg)
print("Grade:", grade)

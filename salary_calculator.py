#salary calculator
x = 40
y = 1.5
z = 10
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate: "))
if hours > x:
    pay = (x * rate) + (hours - x) * (rate * y)
else:
    pay = hours
print("Pay: ", pay, "€")
if hours > z:
    print("You worked overtime")
else:
    print("You did not work overtime")
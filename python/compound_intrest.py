# Compound Interest Calculator

p = float(input("Enter the Principal Amount: "))
r = float(input("Enter the Rate of Interest: "))
t = float(input("Enter the Time (in years): "))

# Calculate Amount
amount = p * (1 + r / 100) ** t

# Calculate Compound Interest
ci = amount - p

print("Compound Interest =", round(ci, 2))
print("Total Amount =", round(amount, 2))

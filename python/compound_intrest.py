choice = input("Enter SI for Simple Interest or CI for Compound Interest: ")

principal = float(input("Enter Principal Amount: "))
time = float(input("Enter Time (Years): "))

if choice == "SI":
    simple_interest = (principal * 2 * time) / 100
    total = principal + simple_interest

    print("Simple Interest =", simple_interest)
    print("Total Amount =", total)

elif choice == "CI":
    amount = principal * (1 + 2 / 100) ** time
    compound_interest = amount - principal

    print("Compound Interest =", compound_interest)
    print("Total Amount =", amount)

else:
    print("Invalid Choice")
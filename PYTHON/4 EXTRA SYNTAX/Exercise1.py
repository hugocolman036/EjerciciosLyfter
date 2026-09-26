price = float(input("Enter the price:\n"))
# Condition
if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.1

final_price = price - discount

print(f"The discount is: {discount}")
print(f"The final price is: {final_price}")
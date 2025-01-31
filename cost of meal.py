ASSUME_TAX = 0.08
TIPS = 0.15

def calculate_bill(amount):
    ass_tax = ASSUME_TAX * amount
    tips = TIPS * amount
    
    total_bill = amount + ass_tax + tips
    return total_bill

amount = float(input("Enter the amount of the bill:"))
total_bill = calculate_bill(amount)
print(f"The total bill is: {total_bill}")

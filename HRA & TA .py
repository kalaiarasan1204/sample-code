# Define constants for HRA and TA
HRA_RATE = 0.10  # HRA is 10% of basic pay
TA_RATE = 0.05   # TA is 5% of basic pay

def calculate_salary(basic_pay):
    # Calculate HRA and TA
    hra = HRA_RATE * basic_pay
    ta = TA_RATE * basic_pay
    
    # Calculate total salary
    total_salary = basic_pay + hra + ta
    
    return total_salary

# Get basic pay from user
basic_pay = float(input("Enter the basic pay of the employee: "))

# Calculate salary
salary = calculate_salary(basic_pay)

# Print the result
print(f"The total salary of the employee is: {salary}")

def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):
    """
    Calculate the net salary after tax based on hourly rate and hours worked.

    Parameters:
    hourly_rate (float): The hourly wage of the employee.
    hours_worked (float): The total hours worked by the employee.
    tax_rate (float): The tax rate to be applied on the gross salary (default is 15%).

    Returns:
    float: The net salary after tax.
    """
    # Compute gross salary
    gross_salary = hourly_rate * hours_worked
    
    # Deduct tax from gross salary
    tax_deduction = gross_salary * tax_rate
    net_salary = gross_salary - tax_deduction
    
    return net_salary

# Main program to drive function execution
def main():
    # Prompt user for input
    try:
        hourly_rate = float(input("Enter hourly rate: "))
        hours_worked = float(input("Enter hours worked: "))
        
        # Input validation
        if hourly_rate < 0 or hours_worked < 0:
            print("Hourly rate and hours worked must be non-negative.")
            return
        
        # Calculate net salary
        net_salary = calculate_salary(hourly_rate, hours_worked)
        
        # Print formatted net salary
        print(f"Net Salary: {net_salary:,.2f}")
    
    except ValueError:
        print("Please enter valid numeric values.")

# Run the main function
if __name__ == "__main__":
    main()
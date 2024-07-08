"""
A simple calculator program to perform basic arithmetic operations.
"""

def add(x, y):
    """
    Add two numbers.
    
    Args:
        x (float): First number.
        y (float): Second number.
        
    Returns:
        float: Sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.
    
    Args:
        x (float): First number.
        y (float): Second number.
        
    Returns:
        float: Difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.
    
    Args:
        x (float): First number.
        y (float): Second number.
        
    Returns:
        float: Product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide two numbers.
    
    Args:
        x (float): First number.
        y (float): Second number.
        
    Returns:
        float: Quotient of x and y.
        
    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    """
    Main function to perform calculator operations.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice. Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

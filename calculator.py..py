def simple_calculator():
    print("Welcome to the python Calculator!")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            operator = input("Enter operator (+, -, *, /, %, **): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero!"
            elif operator == '%':
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                result = "Invalid operator!"

            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numeric values.")

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

# Run the calculator
simple_calculator()

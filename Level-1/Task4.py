
def add(x, y):
    "Add two numbers."
    return x + y

def subtract(x, y):
    "Subtract two numbers."
    return x - y

def multiply(x, y):
    "Multiply two numbers."
    return x * y

def divide(x, y):
    "Divide two numbers."
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def Calculator():
    while True:
        print('Simple Calculator')    
        # Prompt the user to input two numbers
        try:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
        except ValueError:
            print('Invalid input! Please enter numeric values.')
            return

        # Display operation choices
        print('\nChoose an operation:')
        print('1. Addition (+)')
        print('2. Subtraction (-)')
        print('3. Multiplication (*)')
        print('4. Division (/)')

        # Get user choice
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print('Invalid choice! Please choose a valid operation.')
        
        if input('Do Yo Want To Exit(Y/N):').strip().lower() == 'y':
            print('Existing the Calculator.')
            break
if __name__ == "__main__":
    Calculator()
import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def app():
    if len(sys.argv) != 4:
        return "Invalid operation: Please provide three arguments"

    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        result = add(num1, num2)
        return f"Result of adding {num1} and {num2}: {result}"
    elif operation == "subtract":
        result = subtract(num1, num2)
        return f"Result of subtracting {num2} from {num1}: {result}"
    elif operation == "multiply":
        result = multiply(num1, num2)
        return f"Result of multiplying {num1} by {num2}: {result}"
    else:
        return "Invalid operation: Please choose 'add', 'subtract', or 'multiply'"


result = app()
print(result)

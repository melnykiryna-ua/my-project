import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def app():
    if len(sys.argv) != 4:
        sys.exit(1)

    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        result = add(num1, num2)
        print(f"Result of adding {num1} and {num2}: {result}")
    elif operation == "subtract":
        result = subtract(num1, num2)
        print(f"Result of subtracting {num2} from {num1}: {result}")
    else:
        print("Invalid operation")


app()

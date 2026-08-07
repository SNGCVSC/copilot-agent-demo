import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def validate_numeric(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid number")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    parser.add_argument("x", type=validate_numeric, help="First number")
    parser.add_argument("y", type=validate_numeric, help="Second number")
    return parser.parse_args()


def main():
    args = parse_args()
    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    func = ops[args.operation]
    try:
        result = func(args.x, args.y)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(result)


if __name__ == "__main__":
    main()

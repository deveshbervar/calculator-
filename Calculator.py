# Simple CLI Calculator
# List to store calculation history in memory
history = []

# Function to validate numbers
def is_valid_number(num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False

# Calculator operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Divide by zero!" if b == 0 else a / b
def power(a, b): return a ** b

# Main calculator function
def calculator():
    print("SimpleCalc: Commands: add (+), subtract (-), multiply (*), divide (/), power (^), history, exit")

    while True:
        parts = input("\nCommand: ").lower().strip().split()
        if not parts:
            print("Enter a command!")
            continue

        command = parts[0]
        # Map aliases to commands
        command_map = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide", "^": "power"}
        command = command_map.get(command, command)

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "history":
            print("\nHistory:" if history else "No calculations yet!")
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry}")
        elif command in ["add", "subtract", "multiply", "divide", "power"]:
            if len(parts) != 3 or not (is_valid_number(parts[1]) and is_valid_number(parts[2])):
                print(f"Usage: {command} <num1> <num2>")
                continue
            num1, num2 = float(parts[1]), float(parts[2])
            op_map = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide, "power": power}
            result = op_map[command](num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                result_str = f"{num1} {command} {num2} = {result:.2f}"
                print(result_str)
                history.append(result_str)
        else:
            print("Invalid command! Use add, +, subtract, -, multiply, *, divide, /, power, ^, history, exit")

if __name__ == "__main__":
    try:
        calculator()
    except KeyboardInterrupt:
        print("\nTerminated.")
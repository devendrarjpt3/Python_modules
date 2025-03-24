 import sys

def sumOf():
    try:
        if len(sys.argv) < 2:
            print("Usage: python script.py num1 num2 ")
            echo $?
            sys.exit(1)  # Exit with an error code
        numbers = [float(arg) for arg in sys.argv[1:]]
        result = sum(numbers)
        print("Sum of numbers:", result)
    except ValueError:
        print("Error: Please enter valid numbers.")
        sys.exit(2)  # Exit with a different error code

if __name__ == "__main__":
    sumOf()

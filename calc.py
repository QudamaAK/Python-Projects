def add(x, y):
     return x + y

def subtract(x, y):
     return x - y

def multiply(x, y):
     return x * y

def divide(x, y):
     if y == 0:
         return "Error: Division by zero"
     return x / y

def calculator():
     print("Simple CLI Calculator")
     print("Operations: add, subtract, multiply, divide")
     while True:
         operation = input("Enter operation (or 'quit' to exit): ").strip().lower()
         if operation == 'quit':
             break
         if operation not in ['add', 'subtract', 'multiply', 'divide']:
             print("Invalid operation. Please try again.")
             continue
         try:
             x = float(input("Enter first number: "))
             y = float(input("Enter second number: "))
         except ValueError:
             print("Invalid input. Please enter numeric values.")
             continue
         if operation == 'add':
             result = add(x, y)
         elif operation == 'subtract':
             result = subtract(x, y)
         elif operation == 'multiply':
             result = multiply(x, y)
         elif operation == 'divide':
             result = divide(x, y)
         print(f"Result: {result}")

if __name__ == "__main__":
     calculator()

    

def get_number():
    while True:
        try:
            return float(input("Enter number: "))
        except ValueError:
            print("Invalid input")
            
            
def print_menu():
    print("\n====== SMART CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Factorial")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
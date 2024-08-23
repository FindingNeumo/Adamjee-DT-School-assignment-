no1 = int(input("Enter 1st number: "))
no2 = int(input("Enter 2nd number: "))
no3 = int(input("Enter 3rd number: "))
no4 = int(input("Enter 4th number: "))

operation = input("Enter '+' for Addition and 'x' for Multiplication: ").strip()

if operation == '+':
    result = no1 + no2 + no3 + no4
    print(▄▀█ █▀▄▀█ █░░ ▄▀█ █▄░█)
    print(█▀█ █░▀░█ █▄▄ █▀█ █░▀█)
    print('Addition =', result)
elif operation == 'x':
    result = no1 * no2 * no3 * no4
    print('Multiplication =', result)
else:
    print("Invalid input! Please enter '+' for Addition or 'x' for Multiplication.")

def main():
    number = int(input("Enter a number: "))
    
    if 1 <= number <= 2000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        operation = input("Enter '+' for addition or 'x' for multiplication: ")
        value = int(input("Enter the value: "))
        
        if operation == '+':
            result = number + value
        elif operation == 'x':
            result = number * value
        else:
            print("Invalid operation.")
            return
        print("Credits: Created by Amlan Rahaman (Roll 15)")
        print(f"Result: {result}")
    else:
        print("Please enter a valid four-digit number.")

if __name__ == "__main__":
    main()

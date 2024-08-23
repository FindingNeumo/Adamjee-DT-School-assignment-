def main():
    number = int(input("Enter a 4 digit number number: "))
    
    if 1000 <= number <= 9999:
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
        print("Please enter a valid 4 digit number.")

if __name__ == "__main__":
    main()
    

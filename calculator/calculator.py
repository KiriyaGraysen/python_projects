def logic():
    result = 0
    question = ""
    
    while True:
        print("\n[1] Add")
        print("[2] Subtract")
        print("[3] Multiply")
        print("[4] Divide")
        print("[5] Exit")
        choice = int(input("Please choose an operator: "))
        
        if choice == 5:
            break
        
        if question != 'y':
            firstNum = int(input("\nEnter the first number: "))
            
        secondNum = int(input("Enter the second number: "))
        
        match choice:
            case 1:
                result = add(firstNum, secondNum)
            case 2:
                result = subtract(firstNum, secondNum)
            case 3:
                result = multiply(firstNum, secondNum)
            case 4:
                result = divide(firstNum, secondNum)
            case _:
                print("Invalid input.")
        
        question = input("Do you want to use the result as the first number? (y/n): ").lower()
        
        if question == "y":
            firstNum = result
        else:
            result = 0
            
def add(firstNum, secondNum):
    result = firstNum + secondNum
    print(f"{firstNum} + {secondNum} = {result}")
    return result
    
def subtract(firstNum, secondNum):
    result = firstNum - secondNum
    print(f"{firstNum} - {secondNum} = {result}")
    return result
    
def multiply(firstNum, secondNum):
    result = firstNum * secondNum
    print(f"{firstNum} * {secondNum} = {result}")
    return result
    
def divide(firstNum, secondNum):
    if secondNum == 0:
        print("Divisor cannot be zero.")
        return 0
    else:
        result = firstNum / secondNum
        print(f"{firstNum} / {secondNum} = {result}")
        return result
    
    
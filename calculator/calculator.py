def logic():
    result = 0
    question = ""
    
    while True:
        if question != 'y':
            firstNum = int(input("\nEnter the first number: "))
        
        choice = input("Please choose an operator: ")
        
        if choice == 5:
            break
        
        secondNum = int(input("Enter the second number: "))
        
        match choice:
            case "+":
                result = add(firstNum, secondNum)
            case "-":
                result = subtract(firstNum, secondNum)
            case "*":
                result = multiply(firstNum, secondNum)
            case "/":
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
    
    
import random

print("Welcome to number guesser game!")

scores = []
while True:
    print("\nPlease pick 2 number to identify the range of the number")
    
    a = int(input("First number: "))
    b = int(input("Second number: "))
    
    if a > b:
        c = a
        a = b
        b = c
    
    num = random.randint(a, b)
    
    num_guess = 0
    while True:
        num_guess += 1
        guess = int(input(f"\nGuess the number from {a} to {b}: "))
        
        if guess > num:
            print("Lower!")
        elif guess < num:
            print("Higher!")
        elif guess == num:
            print("Congrats!")
            break
    
    print(f"\nTotal guess: {num_guess}")
    
    try_again = int(input("\n[1] Yes\n[2] No\nDo you want to try again?: "))
    
    scores.append(num_guess)
    scores.sort()
    
    print("************************")
    print("\nScores")
    i = 1
    for score in scores:
        print(f"[{i}] {score}")
        i += 1
    print("************************")
    
    if try_again == 2:
        break
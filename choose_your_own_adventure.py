user_name = input("Type your name: ")
print(f"Welcome {user_name} to this adventure!")

answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? Type left to go left and right to go right: ").lower()

if answer == "left":
    answer = input("\nYou come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("\nYou swam across and were eaten by an alligator.")
        
    elif answer == "walk":
        print("\nYou walked for many miles, ran out of water and you lost the game.")
        
    else:
        print("\nNot a valid option. You loser.")
    
elif answer == "right":
    answer = input("\nYou come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        
        if answer == "yes":
            print("\nYou talked the stranger and they give you gold. You WIN!")
            
        elif answer == "no":
            print("\nYou ignore the stranger and they are offended and you lose.")

        else:
            print("\nYou go back and lose.")

    elif answer == "back":
        print("\nYou go back and lose.")

    else:
        print("\nNot a valid option. You loser.")
    
else:
    print("\nNot a valid option. You loser.")

print(f"Thank you for trying {user_name}")

score = 0
highscore = 0
decision = "yes"

name = input("Type your name: ")

print("\nWelcome to my computer quiz,", name + "!")

playing = input("\nDo you want to play? ")

if playing.lower() != "yes":
    print("\nComputer quiz ending...")
    quit()

print("\nOkay! Let's play :)")

while decision.lower() == "yes":
    answer = input("\nWhat does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("\nWhat is RA 1425? ")
    if answer.lower() == "rizal law":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("\nWhat is the hottest planet in the solar system? ")
    if answer.lower() == "venus":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nYou got " + str(score) + " questions correct!")
    print("You got " + str((score / 3) * 100) + "%")
    if highscore > score:
        print("Highscore:", highscore)
    else:
        highscore = score
        print("New highscore:", highscore)

    score = 0

    decision = input("\nDo you want to play again? ")

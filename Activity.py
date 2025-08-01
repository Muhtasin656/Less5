import random
play=True
number=str(random.randint(0,20))
while play:
    guess=input("enter a number between 0 to 20")
    if number==guess:
        print("you have won the game and the number was",number)
        break
    else:
        print("try a again your answer was incorrect")
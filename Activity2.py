import random
while True:
    user=input("enter r for rock s for sissor p for paper")
    possible_action=["r","s","p"]
    computer=random.choice(possible_action)
    print(f"you have chosen {user} the computer have chosen {computer}")
    if user==computer:
        print("its a tie")
    elif user=="r":
        if computer=="s":
            print("you have won")
        else:
            print("you have lost")
    elif user=="p":
        if computer=="r":
            print("you have won")
        else:
            print("you have lost")
    elif user=="s":
        if computer=="p":
            print("you have won")
        else:
            print("you have lost")
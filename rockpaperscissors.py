from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"   
else: 
    computer = "scissors"
print(f"Computer plays {computer}" )

if player == computer:
    print("It's a tie")

elif player == "rock":
    if computer == "scissors":
        print("You win!")
    elif computer == "paper":
        print("The Computer wins!")
    
elif player == "paper":
    if computer == "rock":
        print("You win!")
    elif computer == "scissors":
        print("The Computer wins!")

elif player == "scissors":
    if computer == "paper":
        print("You win!")
    elif computer == "rock":
        print("The Computer wins!")

else:
    print("Please enter a valid move")

    
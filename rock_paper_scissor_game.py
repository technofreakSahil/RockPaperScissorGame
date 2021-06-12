import random
options = ["rock","paper","scissor"]
user_count = 0
comp_count = 0
while True:
    user_input=input(("Type Rock/Paper/Scissor or Q to quit: ")).lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2)
    comp_move = options[random_num]
    print("Comp choosed" , comp_move)
    if user_input == comp_move:
        print("Draw")
    if user_input == "rock" and comp_move == "paper":
        print("You lost")
        comp_count =+1
    if user_input == "rock" and comp_move == "scissor":
        print("You won")
        user_count =+1    
    if user_input == "paper" and comp_move == "rock":
        print("You won")
        user_count =+1        
    if user_input == "paper" and comp_move == "scissor":
        print("You lost")
        comp_count =+1
    if user_input == "scissor" and comp_move == "rock":
        print("You lost")
        comp_count =+1   
    if user_input == "scissor" and comp_move == "paper":
        print("You won")
        user_count =+1
print("User won", user_count ,  "times")
print("Comp won", comp_count ,  "times")
print("End")        
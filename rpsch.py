import random
import time

#There are people watching me

is_running = True
while True:
    while True:
        human_input = input("Enter rock, paper, or scissors: ")
        if human_input != 'rock' and human_input != 'scissors' and human_input != 'paper':
            print("Wrong Input")
            human_input = input("Please enter rock, paper, or scissors: ")
        else:
            break
    time.sleep(1)        
    computer_input = random.randint(1,3)

    if computer_input == 1:
        computer_input = 'scissors'
    elif computer_input == 2:
        computer_input = 'rock'
    else:
        computer_input = 'paper'

    if human_input == computer_input:
        print(f"Its a Tie! Player and Computer chose {computer_input}")
    
    elif (human_input == 'rock' and computer_input == 'scissors') or \
         (human_input == 'scissors' and computer_input == 'paper') or \
         (human_input == 'paper' and computer_input == 'rock'):
        print(f"You win! Player chose {human_input} and Computer chose {computer_input}")
        break
    else:
        print(f"You lose! Player chose {human_input} and Computer chose {computer_input}")
        break
    





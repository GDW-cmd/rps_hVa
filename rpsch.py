import random
import time

input_check = True
run_game = True

def get_human_input():
    is_running = True
    while is_running:
        human_input = input("Enter rock, paper, or scissors: ").lower()
        if human_input in ['rock', 'paper', 'scissors']:
            return human_input
        else:
            print("Entered the wrong input, please enter rock, paper, or scissors: ")


is_running = True

while is_running:
    human_input = get_human_input()
    computer_input = random.randint(1, 3)

    if computer_input == 1:
        computer_input = 'scissors'
    elif computer_input == 2:
        computer_input = 'rock'
    else:
        computer_input = 'paper'

    if computer_input == human_input:
        print(f"It's a Tie! Player and Computer chose {computer_input}")

    elif (human_input == 'rock' and computer_input == 'scissors') or \
         (human_input == 'scissors' and computer_input == 'paper') or \
         (human_input == 'paper' and computer_input == 'rock'):
        print(f"You win! Player chose {human_input} and Computer chose {computer_input}")
        is_running = False

    else:
        print(f"You lose! Player chose {human_input} and Computer chose {computer_input}")
        is_running = False
import random

welcome_message = 'Please choose from rock, paper and scissors.'
prompt = 'Type the exact word in lower-case.  '
tie_message = 'Oups, you chose the same...Tie.'
invalid_message = "Seems you've entered an invalid value."
again_message = 'Please play again.'
choices = ['rock', 'paper', 'scissors']

# game starts
player_choice = 'player'
pc_choice = 'PC'

while player_choice == pc_choice:
    print(tie_message)
    print(again_message)
    print(welcome_message)
    player_choice = input(prompt)

    while (player_choice != 'rock' and
        player_choice != 'paper' and
        player_choice != 'scissors'):
        print(invalid_message)
        print(again_message)
        print(welcome_message)
        player_choice = input(prompt)
    pc_choice = random.choice(choices)
    print(pc_choice)

if ((pc_choice == 'rock' and player_choice == 'scissors') or
    (pc_choice == 'scissors' and player_choice == 'paper') or
    (pc_choice == 'paper' and player_choice == 'rock')) :
        winner = 'PC'
else:
    winner = 'You'

print('You chose', player_choice, 'and PC chose', pc_choice)
print(winner, 'won.')

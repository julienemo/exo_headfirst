import random

prompt = ('Please choose rock, paper and scissors.  ')
choices = ['rock', 'paper', 'scissors']

player_choice = 'player'

while (player_choice != 'rock' and
    player_choice != 'paper' and
    player_choice != 'scissors') :
        player_choice = input(prompt)

pc_choice = random.choice(choices)

if player_choice == pc_choice:
    winner = 'Tie'
elif ((pc_choice == 'rock' and player_choice == 'paper') and
    (pc_choice == 'paper' and player_choice == 'scissors') and
    (pc_choice == 'scissors' and player_choice == 'rock')):
        winner = 'PC'
else:
    winner = "You"

if winner == 'Tie':
    print('Tie. You both chose', pc_choice + '.')
else:
    print(winner, 'won. The computer chose', pc_choice, 'and you', player_choice)


print(player_choice, pc_choice)

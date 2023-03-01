human_turn = 'rock'
computer_turn = 'paper'

if human_turn == computer_turn:
    print('Neizskirts bomar!')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print('Human gets a W!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('Human gets a W!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('Human gets a W')
else:
    print('Fat L!')

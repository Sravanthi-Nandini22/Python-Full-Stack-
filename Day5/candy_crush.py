moves = 15
winning_point = int(input('Tell me how many moves is required to win the game:'))

while moves >= 1:
    if 15 - winning_point == moves:
        print('You won the Game')
        break
    print(f'{moves} are Left')
    moves -= 1
else:
    print('Game over')

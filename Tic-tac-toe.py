import os

os.system('cls' if os.name == 'nt' else 'clear')
print('This is a Tic Tac Toe game \nX starts ')
Point, Turn, Player, Pos = [0, 0], True, [input('What is the name of player 1? (X) '),
                                          input('What is the name of player 2? (O) ')], [str(x) for x in range(10)]
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('       |       |             {} point {}     {} point {}\n   {}   |   {}   |   {}   \n       |       |      '
          ' \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       '
          '\n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n'
          '       |       |       '.format(Player[0], Point[0], Player[1], Point[1], Pos[7], Pos[8], Pos[9], Pos[4],
                                           Pos[5], Pos[6], Pos[1], Pos[2], Pos[3]))
    while True:
        try:
            Move = int(input())
            if Pos[Move] == str(Move):
                break
            else:
                print('That is not a possible move! ')
        except ValueError:
            print('That is not a possible move! ')
    Pos[Move] = 'X' if Turn else 'O'
    Turn = not Turn
    os.system('cls' if os.name == 'nt' else 'clear')
    if Pos[1] == Pos[2] == Pos[3] or Pos[4] == Pos[5] == Pos[6] or Pos[7] == Pos[8] == Pos[9] or Pos[1] == Pos[5] \
            == Pos[9] or Pos[7] == Pos[5] == Pos[3] or Pos[1] == Pos[4] == Pos[7] or Pos[2] == Pos[5] == Pos[8] or \
            Pos[3] == Pos[6] == Pos[9]:
        print(Player[Turn] + ' won! ')
        Point[Turn] += 1
        Pos = [str(x) for x in range(10)]
        input()
    elif all([str(x + 1) != Pos[x + 1] for x in range(9)]):
        print('Draw! ')
        Pos = [str(x) for x in range(10)]
        input()

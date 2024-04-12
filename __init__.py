import os
from ticTacToe.game_play import *
import time


def clear():
    """Helps Clear the Output Console"""
    os.system('clear')


value = None

while True:
    clear()
    print('TIC\tTAC\tTOE\n')
    request = input(
        '''Game Set
1 - Game of 3
2 - Game of 5
3 - Game of 7
4 - Fun Play
>>> ''')
    if request == '1':
        value = 3
        Gamers.game_value = value
        break
    elif request == '2':
        value = 5
        Gamers.game_value = value
        break
    elif request == '3':
        value = 7
        Gamers.game_value = value
        break
    elif request == '4':
        value = 10
        Gamers.game_value = value
        break
    elif request.lower == 'quit':
        quit()
    else:
        print('\nWrong Input. Wait three seconds to re-capture')
        time.sleep(3)
        continue

clear()

play()

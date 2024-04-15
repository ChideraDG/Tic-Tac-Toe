import os
from gamers import *
import time


def clear():
    """Helps Clear the Output Console"""
    os.system('clear')


def play():
    """The Entire Tic-Tac-Toe GamePlay"""
    i = 1  # iterate over each set
    game_input = 0  # helps check for game input in case of a tie
    _numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # numbers in the tic-tac-toe box

    def tie():
        """When the game is a tie"""
        if game_input == 9 and Game.checking() is False:
            clear()
            return True
        else:
            return False

    while i <= Game.game_value:
        Game.game_set = i  # helps the class know which game set is currently being played
        Game.game_selection()  # users shape selection
        while not Game.checking() and game_input < 9:
            # When there is no winner yet
            for key, val in Gamers.shapes.items():
                # iterates for each user to play
                while True:
                    clear()
                    Game.play()  # the tic-tac-toe box
                    Game.ques(key, val)  # question of which place to insert shape
                    _input = input('>>> ')
                    if _input not in _numbers:
                        # in case of an input error
                        print('\nWrong Input. Wait three seconds to re-capture')
                        time.sleep(3)
                        continue
                    elif _input in _numbers:
                        Game.position[f'pos{_input}'] = val  # replace each number in the box with the appropriate shape
                        game_input += 1  # increases game input in case of a tie
                        break
                    elif _input == 'quit':
                        quit()
                if Game.checking() is True:
                    break
                if tie():
                    # The set is a tie and I want to replay the set
                    Game.play()  # the tic-tac-toe box
                    print('\nGame is a Tie. No winner!\nTry again.')
                    time.sleep(3)
                    for number in _numbers:
                        Game.position[f'pos{number}'] = number
                    break
        if tie():
            # The set is a tie and I want to replay the set
            game_input = 0
            continue
        else:
            Game.play()  # the tic-tac-toe box
            i += 1  # increases the set value (enters next set)
            Game.winner()  # checks for winner of the previous set
            print(f'Wait 3 secs to Set {i}')
            time.sleep(3)
            for number in _numbers:
                # Reset the numbers in the tic-tac-toe box
                Game.position[f'pos{number}'] = number
            game_input = 0  # reset the game inputs to zero


class Game(Gamers):
    position = {'pos1': '1', 'pos2': '2', 'pos3': '3', 'pos4': '4', 'pos5': '5',
                'pos6': '6', 'pos7': '7', 'pos8': 8, 'pos9': '9'}

    @classmethod
    def ques(cls, player, shape):
        print(f"""
{player}: Choose where you want to place your {shape}""")

    @classmethod
    def play(cls):
        """The Tic-Tac-Toe box"""
        print('\t - - - - - - - - -')
        print('\t|  {}  |  {}  |  {}  |'.format(cls.position['pos1'], cls.position['pos2'], cls.position['pos3']))
        print('\t - - - - - - - - -')
        print('\t|  {}  |  {}  |  {}  |'.format(cls.position['pos4'], cls.position['pos5'], cls.position['pos6']))
        print('\t - - - - - - - - -')
        print('\t|  {}  |  {}  |  {}  |'.format(cls.position['pos7'], cls.position['pos8'], cls.position['pos9']))
        print('\t - - - - - - - - -')

    @classmethod
    def checking(cls):
        """Checks the winning diagonal and returns a boolean"""
        if cls.position['pos1'] is cls.position['pos2'] and cls.position['pos1'] is cls.position['pos3']:
            cls.winning_shape = cls.position['pos1']
            return True
        elif cls.position['pos4'] is cls.position['pos5'] and cls.position['pos4'] is cls.position['pos6']:
            cls.winning_shape = cls.position['pos4']
            return True
        elif cls.position['pos7'] is cls.position['pos8'] and cls.position['pos7'] is cls.position['pos9']:
            cls.winning_shape = cls.position['pos7']
            return True
        elif cls.position['pos1'] is cls.position['pos4'] and cls.position['pos1'] is cls.position['pos7']:
            cls.winning_shape = cls.position['pos1']
            return True
        elif cls.position['pos2'] is cls.position['pos5'] and cls.position['pos2'] is cls.position['pos8']:
            cls.winning_shape = cls.position['pos2']
            return True
        elif cls.position['pos3'] is cls.position['pos6'] and cls.position['pos3'] is cls.position['pos9']:
            cls.winning_shape = cls.position['pos3']
            return True
        elif cls.position['pos1'] is cls.position['pos5'] and cls.position['pos1'] is cls.position['pos9']:
            cls.winning_shape = cls.position['pos1']
            return True
        elif cls.position['pos3'] is cls.position['pos5'] and cls.position['pos3'] is cls.position['pos7']:
            cls.winning_shape = cls.position['pos3']
            return True
        else:
            return False

    @classmethod
    def game_selection(cls):
        """Allocates shapes to each player"""
        while True:
            clear()
            print(f'\tGame Set {Game.game_set}\n')
            ques = input(
                '''Player 1 pick your sign ( X or O ) 
>>> ''')
            if ques.lower() == 'x':
                Gamers.shapes['Player 1'] = 'X'
                Gamers.shapes['Player 2'] = 'O'
                break
            elif ques.lower() == 'o':
                Gamers.shapes['Player 1'] = 'O'
                Gamers.shapes['Player 2'] = 'X'
                break
            elif ques.lower() == 'quit':
                quit()
            else:
                print('\nWrong Input. Wait three seconds to re-capture')
                time.sleep(3)
                continue

class Gamers:
    """Control the Gamers' activities"""
    game_value = 0  # The Players' total set
    no_of_players = 2  # Number of Players
    game_set = 1  # The Game current set
    __scores = {'Player 1': 0, 'Player 2': 0}  # scores of each player
    shapes = {'Player 1': 'X', 'Player 2': 'O'}  # shape of each player
    __winning_shape = None  # takes in the winning shape after each set

    @classmethod
    def winner(cls):
        """Checks for the winner after each set and after total set"""
        if cls.shapes['Player 1'] == cls.__winning_shape:
            print(f'Player 1 is the winner of Set {cls.game_set}\n')
            cls.__scores['Player 1'] += 1
        elif cls.shapes['Player 2'] == cls.__winning_shape:
            print(f'Player 2 is the winner of Set {cls.game_set}\n')
            cls.__scores['Player 2'] += 1

        if cls.__scores['Player 1'] + cls.__scores['Player 2'] == cls.game_value:
            if cls.__scores['Player 1'] > cls.__scores['Player 2']:
                print(f'Player 1 is the winner')
                quit()
            else:
                print(f'Player 2 is the winner')
                quit()

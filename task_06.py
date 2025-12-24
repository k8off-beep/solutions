players = [['player1', 'P'], ['player2', 'S']]
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(lst):
    if len(lst) != 2:
        raise WrongNumberOfPlayersError
    if lst[0][1] not in 'PSR' or lst[1][1] not in 'PSR':
        raise NoSuchStrategyError
    if lst[0][1] == lst[1][1]:
        #print(f'{lst[0][0]} {lst[0][1]}')
        print('Player 1 is winner')
    if lst[0][1] == 'P' and lst[1][1] == 'S':
        print('Player 2 is winner')
    if lst[0][1] == 'S' and lst[1][1] == 'P':
        print('Player 1 is winner')
    if lst[0][1] == 'P' and lst[1][1] == 'R':
        print('Player 1 is winner')
    if lst[0][1] == 'R' and lst[1][1] == 'P':
        print('Player 2 is winner')
    if lst[0][1] == 'S' and lst[1][1] == 'R':
        print('Player 2 is winner')
    if lst[0][1] == 'R' and lst[1][1] == 'S':
        print('Player 1 is winner')




rps_game_winner([['player1', 'P'], ['player2', 'S']])

rps_game_winner([['player1', 'P'], ['player2', 'P']])
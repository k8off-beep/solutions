class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if isinstance(players, tuple) and len(players) == 1:
        players = players[0]
    
    if len(players) != 2:
        raise WrongNumberOfPlayersError
    
    p1_name, p1_move = players[0]
    p2_name, p2_move = players[1]
    
    valid_moves = {'R', 'P', 'S'}
    if p1_move not in valid_moves or p2_move not in valid_moves:
        raise NoSuchStrategyError
    
    win_conditions = {
        'R': 'S', 
        'S': 'P', 
        'P': 'R'   
    }
    
    if p1_move == p2_move:
        return f"{p1_name} {p1_move}"
    
    if win_conditions[p1_move] == p2_move:
        return f"{p1_name} {p1_move}"
    else:
        return f"{p2_name} {p2_move}"


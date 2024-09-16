# RPS_game.py

import random

def play(player1, player2, num_games=1000, verbose=False):
    player1_score = 0
    player2_score = 0
    player1_history = []
    player2_history = []
    
    for i in range(num_games):
        player1_move = player1(player2_history[-1] if player2_history else '')
        player2_move = player2(player1_history[-1] if player1_history else '')
        
        player1_history.append(player1_move)
        player2_history.append(player2_move)
        
        if verbose:
            print(f"Game {i+1}: Player 1: {player1_move} | Player 2: {player2_move}")
        
        if (player1_move == 'R' and player2_move == 'S') or \
           (player1_move == 'S' and player2_move == 'P') or \
           (player1_move == 'P' and player2_move == 'R'):
            player1_score += 1
        elif player1_move != player2_move:
            player2_score += 1
    
    print(f"Final score: Player 1: {player1_score} | Player 2: {player2_score}")
    print(f"Player 1 win rate: {player1_score / num_games:.2%}")

# Example bots
def quincy(prev_play, opponent_history=[]):
    quincy_sequence = ['R', 'P', 'S', 'R', 'P', 'S']
    return quincy_sequence[len(opponent_history) % len(quincy_sequence)]

def abigail(prev_play, opponent_history=[]):
    if prev_play == '':
        return 'R'
    if prev_play == 'R':
        return 'P'
    if prev_play == 'P':
        return 'S'
    return 'R'

def kriss(prev_play, opponent_history=[]):
    return random.choice(['R', 'P', 'S'])

def mrugesh(prev_play, opponent_history=[]):
    if len(opponent_history) < 2:
        return 'R'
    last_two = opponent_history[-2:]
    if last_two == ['R', 'R'] or last_two == ['S', 'S'] or last_two == ['P', 'P']:
        return 'P'
    if last_two == ['R', 'S'] or last_two == ['S', 'P'] or last_two == ['P', 'R']:
        return 'R'
    return 'S'

# RPS.py

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Simple random choice as a starting point
    return random.choice(['R', 'P', 'S'])

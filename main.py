# main.py

from RPS_game import play, quincy, abigail, kriss, mrugesh
from RPS import player

if __name__ == "__main__":
    play(player, quincy, 1000, verbose=True)
    play(player, abigail, 1000, verbose=True)
    play(player, kriss, 1000, verbose=True)
    play(player, mrugesh, 1000, verbose=True)
    
    # Uncomment the line below to run the unit tests
    # import test_module; test_module.test()

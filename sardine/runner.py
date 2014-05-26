import sys
from game import Game
from ai_wrapper import AI_Wrapper
from ui_dummy import UI

if __name__ == "__main__":
    ai = AI_Wrapper(sys.argv[1])
    ui = UI()
    game = Game(ui,ai,5)
    game.start()
import sys
from game import Game
from ai_wrapper import AI_Wrapper
from ui import UI

def run():
    ai = AI_Wrapper(sys.argv[1])
    ui = UI()
    game = Game(ui,ai,2)
    game.start()

if __name__ == "__main__":
    run()
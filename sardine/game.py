from board import Board
from ui_dummy import UI

class Game:
    def __init__(self,ui,ai,size):
        self.ui = ui
        self.ai = ai
        self.board = Board.new_empty(size)
        
    def start(self):
        turn = 0
        players = [self.ai,self.ui]
        self.ui.start(self.board)
        while self.not_over():
            self.play(players[turn].play(self.board))
            turn = (turn+1)%2
            self.ui.update(self.board)
        self.ui.end()
        
    def not_over(self):
        return "_" in self.board.to_s()
    
    def play(self, (index, letter)):
        if self.board.board[index] == "_":
            self.board.board[index] = letter
        else:
            raise "You played in an invalid space:\nindex: %d\nin:\n%s\n" % self.board.to_s()
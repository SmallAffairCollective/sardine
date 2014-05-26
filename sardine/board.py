import math

class Board:
    
    @staticmethod
    def parse(string_board):
        '''
        Converts a string of characters into an array.
        '''
        return [char for char in string_board]
    
    @staticmethod
    def new_empty(size):
        return Board("_"*size*size)
        
    def __init__(self,string_board):
        self.board = Board.parse(string_board)
        self.size = int(math.sqrt(len(string_board)))
    
    def to_s(self):
        return ''.join(self.board)
    
    def get(self,row,col):
        return self.board[row*self.size + col]
    
    def set(self,row,col,val):
        self.board[row*self.size + col] = val
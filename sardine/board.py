import math

class Board:
    @staticmethod
    def parse(string_board):
        '''
        Converts a string of characters into an array.

        Used by initializer.
        '''
        return [char for char in string_board]

    @staticmethod
    def new_empty(size):
        '''
        Factory method which reates a new board with all blanks.
        '''
        return Board("_"*size*size)

    @staticmethod
    def calculate_size(board):
        '''
        Given a 1D array representing a board, calculate its size.
        '''
        size = math.sqrt(len(board))
        if size != int(size):
            raise "unacceptable board length"
        else:
            return int(size)

    def __init__(self,string_board):
        # self.board is a listified string
        self.board = Board.parse(string_board)
        self.size = Board.calculate_size(self.board)

    def to_s(self):
        return ''.join(self.board)

    def get(self,row,col):
        return self.board[row*self.size + col]

    def get_row(self, row):
        return self.board[row*self.size:(row*self.size)+self.size]

    def set(self,row,col,val):
        self.board[row*self.size + col] = val

    def draw_padding(self, pad, cell_width):
        return " "*pad + (("|"+(" "*cell_width))*self.size)+"|\n"

    def draw_border(self, cell_width):
        return (("+"+("-"*cell_width))*self.size)+"+\n"

    def draw_char_row(self, cell_width, row_num):
        row = "|"
        row += " "*((cell_width)/2)
        inbetween_string = " "*((cell_width-1)/2)+"|"+(" "*((cell_width)/2))
        row += (inbetween_string).join(self.get_row(row_num))
        row += " "*((cell_width-1)/2)+"|\n"
        return row

    def draw_row(self, pad, cell_height, cell_width, row_num):
        row =  " "*pad + self.draw_border(cell_width)
        row += self.draw_padding(pad, cell_width)*((cell_height-1)/2)
        row += " "*pad + self.draw_char_row(cell_width, row_num)
        row += self.draw_padding(pad, cell_width)*(cell_height/2)
        return row

    def drawable(self, grid_width, grid_height):
        draw_board = ""

        dim = min(grid_width,grid_height*2)
        
        h_padding = (grid_height*2 - dim)/4
        w_padding = (grid_width - dim)/2
        
        cell_height = ((dim/2-1)/self.size)-1
        cell_width = ((dim-2)/self.size)-1
        
        # Draw top padding to center the grid
        draw_board += "\n"*h_padding
        
        # Draw grid
        for row in range(self.size):
            draw_board += self.draw_row(w_padding, cell_height, cell_width, row)
        draw_board += " "*w_padding + self.draw_border(cell_width)

        return draw_board
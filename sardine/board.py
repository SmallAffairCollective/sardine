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
        # self.board is a listified string
        self.board = Board.parse(string_board)
        self.size = math.sqrt(len(string_board))
        if self.size != int(self.size):
            raise "unacceptable board length"
        else:
            self.size = int(self.size)

    def to_s(self):
        return ''.join(self.board)

    def get(self,row,col):
        return self.board[row*self.size + col]

    def get_row(self, row):
        return self.board[row*self.size:(row*self.size)+self.size]

    def set(self,row,col,val):
        self.board[row*self.size + col] = val

    def draw_padding(self, cell_width):
        return (("|"+(" "*cell_width))*self.size)+"|\n"

    def draw_border(self, cell_width):
        return (("+"+("-"*cell_width))*self.size)+"+\n"

    def draw_char_row(self, cell_width, row_num):
        row = "|"
        row += " "*((cell_width)/2)
        inbetween_string = " "*((cell_width)/2)+"|"+(" "*((cell_width-1)/2))
        row += (inbetween_string).join(self.get_row(row_num))
        row += " "*((cell_width-1)/2)+"|\n"
        return row

    def draw_row(self, cell_height, cell_width, row_num):
        row = self.draw_border(cell_width)
        row += self.draw_padding(cell_width)*((cell_height-1)/2)
        row += self.draw_char_row(cell_width, row_num)
        row += self.draw_padding(cell_width)*(cell_height/2)
        return row

    def drawable(self, grid_width, grid_height):
        draw_board = ""
        cell_height = ((grid_height-1)/self.size)-1
        cell_width = ((grid_width-2)/self.size)-1
        for row in range(self.size):
            draw_board += self.draw_row(cell_height, cell_width, row)
        draw_board += self.draw_border(cell_width)
        return draw_board

import curses
import math

class main(object):
    def __init__(self):
        a = "junk"
        self.win = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlighted = curses.color_pair(1)
        self.normal = curses.A_NORMAL

    @classmethod
    def get_param(self, prompt_string):
        self.win.clear()
        self.win.border(0)
        self.win.addstr(2, 2, prompt_string)
        self.win.refresh()
        input = self.win.getstr(10, 10, 60)
        return input

    @classmethod
    def display_menu(self, board):
        x = 0
        position = 0
        board_size = math.sqrt(len(board))
        if board_size != int(board_size):
            print "unacceptable board length"
            curses.endwin()
        else:
            board_size = int(board_size)

        while x != ord('2'):
            draw_board = ""
            self.win = curses.initscr()
            win_tuple = self.win.getmaxyx()
            lines = board_size-1
            square = ((win_tuple[1]-2)/board_size)-lines
            padding = (win_tuple[1]-(square*board_size))/2

            j = 0
            for i in xrange(((square*board_size)+lines)/2):
                if i % (square/2) == (((square/2)-1)/2)+1:
                    if square % 2 == 0:
                        z = "x"
                    else:
                        z = " x"
                else:
                    if square % 2 == 0:
                        z = " "
                    else:
                        z = "  "
                if i % (square/2) == 0:
                    if j <= board_size:
                        draw_board += (" "*padding)+((("-"*(square-len(z)+1))+"+")*lines)+("-"*(square-len(z)+1))+"\n"
                    j += 1
                elif j <= board_size:
                    draw_board += (" "*padding)+(((" "*((square/2)-len(z)))+z+(" "*(square/2))+"|")*lines)+(" "*((square/2)-len(z)))+z+(" "*(square/2))+"\n"

            self.win.clear()
            self.win.addstr(2, 2, "Shall we play a game...", curses.A_STANDOUT)
            self.win.addstr(4, 4, "1 - Take a turn", curses.A_BOLD)
            self.win.addstr(5, 4, "2 - Exit", curses.A_BOLD)
            self.win.addstr(7, 0,  draw_board)
            self.win.refresh()

            x = self.win.getch()

            if x == ord('1'):
                location = self.get_param("Enter a location")
                character = self.get_param("Enter a character")
                curses.endwin()
            elif x == ord('2'):
                curses.endwin()

        curses.endwin()

def start():
    main().display_menu("asdfgasdfgasdfga")

if __name__ == "__main__":
    start()

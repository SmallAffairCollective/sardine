from board import Board
import curses
import math
import sys

class UI(object):
    def __init__(self):
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

        while x != ord('2'):
            self.win = curses.initscr()
            win_tuple = self.win.getmaxyx()
            draw_board = board.drawable(win_tuple[1], win_tuple[0]-8)

            self.win.clear()
            self.win.addstr(2, 2, "Shall we play a game...", curses.A_STANDOUT)
            self.win.addstr(4, 4, "1 - Take a turn", curses.A_BOLD)
            self.win.addstr(5, 4, "2 - Exit", curses.A_BOLD)
            self.win.addstr(7, 0,  draw_board)
            self.win.refresh()

            x = self.win.getch()

            if x == ord('1'):
                location = len(board.board)+1
                while location > len(board.board):
                    location = self.get_param("Enter a location")
                    try:
                        location = int(location)
                    except:
                        location = len(board.board)+1
                character = self.get_param("Enter a character")
                curses.endwin()
            elif x == ord('2'):
                curses.endwin()

        curses.endwin()

def start():
    UI().display_menu(Board("abcdefghijklmnop"))

if __name__ == "__main__":
    start()

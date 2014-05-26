class UI:
    def start(self):
        print "UI START"
    def play(self,board):
        print "play: board"
        ret = raw_input("play: %s" % board.to_s()).split()
        return int(ret[0]),ret[1]
    def display_menu(self,board):
        print board.to_s()
    def end(self):
        print "UI END!"
        
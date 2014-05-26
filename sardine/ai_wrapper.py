import shlex, subprocess

class AI_Wrapper:
    def __init__(self,call):
        # 'parse' the CLI call
        self.call = shlex.split(call)
    
    def play(self,board):
        # run player as a subprocess
        proc = subprocess.Popen(self.call, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        move = proc.communicate(board.to_s())[0].split()
        return int(move[0]), move[1]
class BoardFunctions:
    # To make this function scalable it calls arguments from the main program that define the play board
    def make_board(self, rows, cols):
        play_board = [[' ' for _ in range(cols)] for _ in range(rows)]
        return play_board
    # to make scalable this  I have used the arguments for rows and columns that get defined in the main program
    # to achieve a clean scalable game board I have made the columns variable times it's self by 1.3 other wise
    # the '----------' string falls short once the amount of columns and rows gets large
    def format_board(self,play_board,rows,cols):
        for row in range(rows):
            print('' + ' | '.join(play_board[row]))
            if row < rows-1:
                print('---'*int(cols*1.3))



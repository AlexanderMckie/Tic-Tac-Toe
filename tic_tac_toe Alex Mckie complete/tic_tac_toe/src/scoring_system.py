
class ScoringSystem:

    def check_game(self,play_board, player, grid_layout):
        # To make these scalable for the row and column I used the variable of row and col and have a all() function
        # to compare them against the play_board for the row's it was easy enough but for the columns I had to do a
        # range() count through the columns to pick up the values.
        for row in play_board:
            if all(index == player for index in row):
                return True
        for col in range(len(play_board[0])):
            if all(row[col] == player for row in play_board):
                return True
        # to work out the diagonal win I got the scalable win to work by using the range function to count up for the
        # rows and columns as it follows a pattern (0,0 1,1 2,2 3,3 etc) then i was able to use similar logic to the
        # rows and column winning conditions. With the reverse there is a similar pattern (0,3 1,2 2,1 3,0 etc)
        # I got stuck on how to reverse count the column for the opposite direction so I asked ChatGPT
        # how to reverse count a nested List and refactored it work I have attached a word document with its examples.
        diagonal_index = [play_board[i][i] for i in range(grid_layout)]
        if all(index == player for index in diagonal_index):
            return True
        diagonal_index_opposite = [play_board[i][len(play_board) - i - 1] for i in range(grid_layout)]
        if all(index == player for index in diagonal_index_opposite):
            return True


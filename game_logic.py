class GameLogic:
    board = []

    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ] 
    
    def print_board(self, board):
        for row in board:
            print(" | ".join(row))
            print("-" * (len(row) * 4 - 3))
    def end_game(self):
        print(self.board)
        i = 0
        for row in self.board:
            print("in loop")
            print(row)
            for column in self.board[i]:
                if row == 0:
                    if row[column] == "X" and row[column + 1] == "X" and row[column + 2] == "X":
                        return "X"
                    elif row[column] == "O" and row[column + 1] == "O" and row[column] == "O":
                        return "O"
            i = i + 1
                


import numpy as np
import sys
import os

class GameLogic:
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
    # update board

    def update_board(self, row, col, player):
        if row > 2 or row < 0 or col > 2 or col < 0 or self.board[row][col] != " ":
            return False
        self.board[row][col] = player
        return True
    # print board

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal for updated board
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:  # Only print separator for first two rows
                print("-" * 9)

    # game logic-win/loss/draw conditions

    def end_game(self):
        # vertical win

        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        # horizontal win

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return self.board[0][col]
        # diagonal win (top-left to bottom-right)

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]
        # diagonal win (top-right to bottom-left)

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return self.board[0][2]
        # draw check

        for row in self.board:
            if " " in row:
                return None  
        return "Draw"
    
# AI - Win/Draw

def minimax(board, is_maximizing):
    game_result = board.end_game()
    if game_result == "X":
        return -1   # Losing returns -1
    elif game_result == "O":
        return 1    # Win returns 1
    elif game_result == "Draw": 
        return 0    # Draw returns 0
    
    if is_maximizing:
        best_score = -float('inf')  # Initialize best score to lowest possible value
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == " ":  # Check for empty spot
                    board.board[i][j] = "O"  # AI makes a move
                    score = minimax(board, False)  # Call minimax for minimizing player
                    board.board[i][j] = " "  # Undo move
                    best_score = max(score, best_score)  # Store the best possible score (it wants to win)
        return best_score
    else:
        best_score = float('inf') # Initialize best score to highest possible value
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == " ":
                    board.board[i][j] = "X"
                    score = minimax(board, True)
                    board.board[i][j] = " "
                    best_score = min(score, best_score) # Store the worst possible score (I am X, it wants me to lose)
        return best_score

def best_move(board):
    best_score = -float('inf')  # Initialize best_score to lowest possible value
    move = (-1, -1)  # Initialize move to an invalid position
    
    # Loop through every cell on the board
    for i in range(3):
        for j in range(3):
            # Check if the cell is empty
            if board.board[i][j] == " ":
                # Try placing "O" in the empty cell (AI's move)
                board.board[i][j] = "O"
                
                # Call minimax to evaluate the outcome of this move
                score = minimax(board, False)
                
                # Undo the move (reset the board)
                board.board[i][j] = " "
                
                # If the score is better than the best_score, update best_score and the best move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    
    # If a valid best move was found, apply it to the board
    if move != (-1, -1):
        board.update_board(move[0], move[1], "O")

def main():
    game = GameLogic()
    players = {"X": "Human", "O": "AI"}
    
    while True:
        game.print_board()
        
        if game.end_game():
            result = game.end_game()
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{players[result]} wins!") # Human wins & AI wins...
            break

        if players["X"] == "Human":
            while True:
                try:
                    col = int(input("Enter column (1-3): ")) - 1 #adjust to human numbers
                    row = int(input("Enter row (1-3): ")) - 1
                    if game.update_board(row, col, "X"):
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError: # not a number
                    print("Invalid input! Enter numbers between 1-3.")
        
        game.print_board()
        
        if game.end_game():
            result = game.end_game()
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{players[result]} wins!")
            break
        
        print("AI is making a move...")
        best_move(game) #plays the best move for the AI

if __name__ == "__main__":
    main()
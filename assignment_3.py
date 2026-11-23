
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def check_winner(board, player):
    win = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        all(board[i] == player for i in combo)
        for combo in win
    )

board = [" "] * 9
player = "X"

for turn in range(9):
    print_board(board)

    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

    while pos not in range(9) or board[pos] != " ":
        pos = int(input("Invalid move! Try again: ")) - 1

    board[pos] = player

    if check_winner(board, player):
        print_board(board)
        print("Player", player, "wins!")
        break

    player = "O" if player == "X" else "X"

else:
    print_board(board)
    print("Game Draw!")

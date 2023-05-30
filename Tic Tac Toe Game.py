def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def get_move(board, player):
    while True:
        move = input("Enter your move, {} (row,column): ".format(player))
        row, col = move.split(",")
        row, col = int(row), int(col)
        if board[row][col] == " ":
            return row, col
        else:
            print("That space is already taken. Try again.")

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print_board(board)
    while True:
        row, col = get_move(board, players[current_player])
        board[row][col] = players[current_player]
        print_board(board)
        if check_win(board, players[current_player]):
            print("{} wins!".format(players[current_player]))
            return
        if all(" " not in row for row in board):
            print("It's a tie!")
            return
        current_player = (current_player + 1) % 2

tic_tac_toe()

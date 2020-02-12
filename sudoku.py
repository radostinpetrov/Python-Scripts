example_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()


# We will be using a 0 as a blank/unfilled space
# Returns empty spaces on the boards
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j


# Check whether the given number at the given position is valid
# i.e. whether it complies with the rules of sudoku
def is_valid(board, num, pos):
    # Check for row validity
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and pos[1] != j:
            return False

    # Check for column validity
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 sector validity
    sector_row = pos[0] // 3
    sector_col = pos[1] // 3

    for i in range(sector_row * 3, sector_row * 3 + 3):
        for j in range(sector_col * 3, sector_col * 3 + 3):
            if pos != (i, j):
                return board[i][j] != num


# Solve the board using backtracking algorithm
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
    return False


print_board(example_board)
solve(example_board)
print_board(example_board)
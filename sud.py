# Define the Sudoku as a 2D array
puzzle = [[0, 0], [0, 0]]

# Define a function to print the puzzle
def print_puzzle():
    for row in puzzle:
        print(row)

# Define a function to check if the puzzle is solved
def is_solved():
    for row in puzzle:
        if 0 in row:
            return False
    return True

# Define a function to find the possible values for a cell
def find_possible_values(row, col):
    possible_values = [1, 2]
    for i in range(2):
        if puzzle[i][col] in possible_values:
            possible_values.remove(puzzle[i][col])
        if puzzle[row][i] in possible_values:
            possible_values.remove(puzzle[row][i])
    return possible_values

# Define a function to solve the puzzle
def solve():
    for row in range(2):
        for col in range(2):
            if puzzle[row][col] == 0:
                possible_values = find_possible_values(row, col)
                if len(possible_values) == 1:
                    puzzle[row][col] = possible_values[0]
    if not is_solved():
        solve()

# Example puzzle
puzzle = [[0, 0], [0, 2]]

# Print the puzzle
print_puzzle()

# Solve the puzzle
solve()

# Print the solved puzzle
print("\nSolved puzzle:")
print_puzzle()